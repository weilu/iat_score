import pandas as pd
import gettext
import os.path as path

localedir = path.join(path.abspath(path.dirname(__file__)), 'locale')
print(localedir)
translate = gettext.translation('iat_score', localedir, fallback=False, languages=['es'])
_ = translate.gettext

# TODO: allow specifying column names & rounds & trial numbers per round

class Scorer():
    def __init__(self, default_left_main, default_right_main,
            default_left_sub, default_right_sub):
        self.default_left_main = default_left_main
        self.default_right_main = default_right_main
        self.default_left_sub = default_left_sub
        self.default_right_sub = default_right_sub


    def score(self, data):
        if len(data) != 7:
            raise ValueError(_('There were not enough rounds to determine a result.'))

        dfs = []
        for block in data:
            dfs.append(pd.DataFrame.from_dict(block))
        df = pd.concat(dfs, keys=list(range(1, len(data)+1)))

        # Remove wrong trials, as the subsequent corrected trial contains latency for both
        df = df[df.correct_side == df.pressed_side]

        num_trials = df.shape[0]
        if num_trials < 180: # 20 + 20 + 20 + 40 + 20 + 20 + 40
            raise ValueError(_('There were not enough trials to determine a result.'))

        # Compute D score as describe here:
        # http://faculty.washington.edu/agg/IATmaterials/Summary%20of%20Improved%20Scoring%20Algorithm.pdf

        # Step 1
        df = df[df.elapsed_time <= 10000]

        # Step 2
        num_trials_too_fast = df[df.elapsed_time < 300].shape[0]
        if num_trials_too_fast / num_trials > 0.1:
            raise ValueError(_('There were too many fast trials to determine a result.'))

        # Step 3
        sd3n6 = df[df.index.isin([3, 6], level=0)][['elapsed_time']].std()
        sd4n7 = df[df.index.isin([4, 7], level=0)][['elapsed_time']].std()

        # Step 4
        mean3 = df.loc[3][['elapsed_time']].mean()
        mean4 = df.loc[4][['elapsed_time']].mean()
        mean6 = df.loc[6][['elapsed_time']].mean()
        mean7 = df.loc[7][['elapsed_time']].mean()

        # Step 5
        mean_6_diff_3 = mean6 - mean3
        mean_7_diff_4 = mean7 - mean4

        # Step 6
        d1a = mean_6_diff_3 / sd3n6
        d1b = mean_7_diff_4 / sd4n7

        # Step 7
        d1 = (d1a + d1b) / 2
        if df.loc[1].loc[0, 'left_main_category'] != self.default_left_main:
            d1 = -d1

        return d1.to_list()[0]


    def feedback(self, d1_score):
        association = _('automatic association of ')
        w = _("with")
        n = _("and")
        if d1_score > 0:
            association += f'{self.default_left_main} {w} {self.default_left_sub} {n} {self.default_right_main} {w} {self.default_right_sub}'
        else:
            association += f'{self.default_left_main} {w} {self.default_right_sub} {n} {self.default_right_main} {w} {self.default_left_sub}'

        abs_d1 = abs(d1_score)
        if abs_d1 <= 0.15:
            degree = _('little to no')
        elif abs_d1 > 0.15 and abs_d1 <= 0.35:
            degree = _('a slight')
        elif abs_d1 > 0.35 and abs_d1 <= 0.65:
            degree = _('a moderate')
        else:
            degree = _('a strong')

        data_suggest = _("Your data suggest")
        return f'{data_suggest} {degree} {association}'


if __name__=='__main__':
    scorer = Scorer('Masculino', 'Femenino', 'Familia', 'Carrera')
    print(scorer.feedback(2))

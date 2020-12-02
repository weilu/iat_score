import pandas as pd

# TODO: remove asserts
# TODO: allow specifying column names & trial numbers per round

def score(data, default_main_left):
    assert(len(data) == 7)

    dfs = []
    for block in data:
        dfs.append(pd.DataFrame.from_dict(block))
    df = pd.concat(dfs, keys=list(range(1, len(data)+1)))

    # Remove wrong trials, as the subsequent corrected trial contains latency for both
    df = df[df.correct_side == df.pressed_side]

    num_trials = df.shape[0]
    assert(num_trials == 180) # 20 + 20 + 20 + 40 + 20 + 20 + 40

    # Compute D score as describe here:
    # http://faculty.washington.edu/agg/IATmaterials/Summary%20of%20Improved%20Scoring%20Algorithm.pdf

    # Step 1
    df = df[df.elapsed_time <= 10000]

    # Step 2
    num_trials_too_fast = df[df.elapsed_time < 300].shape[0]
    if num_trials_too_fast / num_trials > 0.1:
        raise ValueError('Too many trials inhumanly fast')

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
    if df.loc[1].loc[0, 'left_main_category'] != default_main_left:
        d1 = -d1

    return d1.elapsed_time

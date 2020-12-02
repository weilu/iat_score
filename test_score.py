import json
import unittest
from score import Scorer

class TestScore(unittest.TestCase):

    def setUp(self):
        self.scorer = Scorer('Masculino', 'Femenino', 'Familia', 'Carrera')

    def test_score(self):
        data = None
        with open('iat.json') as f:
            data = json.load(f)

        d1 = self.scorer.score(data)

        self.assertTrue(d1 <= 2)
        self.assertTrue(d1 >= -2)

    def test_feedback(self):
        self.assertTrue('little to no' in self.scorer.feedback(0))
        self.assertTrue('little to no' in self.scorer.feedback(0.14))

        self.assertTrue('a slight' in self.scorer.feedback(0.16))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(0.16))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(0.34))
        self.assertTrue('a moderate' in self.scorer.feedback(0.36))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(0.36))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(0.64))
        self.assertTrue('a strong' in self.scorer.feedback(0.66))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(0.66))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_left_sub}' in self.scorer.feedback(1.5))

        self.assertTrue('a slight' in self.scorer.feedback(-0.16))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-0.16))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-0.34))
        self.assertTrue('a moderate' in self.scorer.feedback(-0.36))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-0.36))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-0.64))
        self.assertTrue('a strong' in self.scorer.feedback(-0.66))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-0.66))
        self.assertTrue(f'{self.scorer.default_left_main} with {self.scorer.default_right_sub}' in self.scorer.feedback(-1.5))

if __name__ == '__main__':
    unittest.main()

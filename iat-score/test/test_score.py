import json
import os.path as path
import unittest
from score import Scorer

class TestScore(unittest.TestCase):

    def setUp(self):
        self.scorer = Scorer('Masculino', 'Femenino', 'Familia', 'Carrera')

    def test_score(self):
        data = None
        test_data = path.join(path.abspath(path.dirname(__file__)), 'iat.json')
        with open(test_data) as f:
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

        print(self.scorer.feedback(0.1))
        print(self.scorer.feedback(0.16))
        print(self.scorer.feedback(0.36))
        print(self.scorer.feedback(-0.8))

if __name__ == '__main__':
    unittest.main()

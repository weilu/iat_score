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


if __name__ == '__main__':
    unittest.main()

import json
import unittest
from score import score

class TestScore(unittest.TestCase):

    def test_score(self):
        data = None
        with open('iat.json') as f:
            data = json.load(f)

        d1 = score(data, 'Masculino')

        self.assertTrue(d1 <= 2)
        self.assertTrue(d1 >= -2)


if __name__ == '__main__':
    unittest.main()

import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_demoa(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parse()
        answer = demoa.solvea()
        self.assertEqual(37, answer)

    def test_fulla(self):
        fulla = Puzzle("test_data.txt")
        fulla.parse()
        answer = fulla.solvea()
        self.assertEqual(341558, answer)

    def test_demob(self):
        demob = Puzzle("demo_data.txt")
        demob.parse()
        answer = demob.solveb()
        self.assertEqual(168, answer)

    def test_fullb(self):
        fullb = Puzzle("test_data.txt")
        fullb.parse()
        answer = fullb.solveb()
        self.assertEqual(93214037, answer)


if __name__ == '__main__':
    unittest.main()

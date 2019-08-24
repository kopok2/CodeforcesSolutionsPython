import unittest
from unittest.mock import patch

from cdf_722B import CodeforcesTask722BSolution


class TestCDF722B(unittest.TestCase):
    def test_722B_acceptance_1(self):
        mock_input = ['3', '2 2 3', 'intel', 'code', 'ch allenge']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_722B_acceptance_2(self):
        mock_input = ['4', '1 2 3 1', 'a', 'bcdefghi', 'jklmnopqrstu', 'vwxyz']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_722B_acceptance_3(self):
        mock_input = ['4', '13 11 15 15', 'to be or not to be that is the question', 'whether tis nobler in the mind to suffer', 'the slings and arrows of outrageous fortune', 'or to take arms against a sea of troubles']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

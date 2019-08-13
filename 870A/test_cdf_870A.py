import unittest
from unittest.mock import patch

from cdf_870A import CodeforcesTask870ASolution


class TestCDF870A(unittest.TestCase):
    def test_870A_acceptance_1(self):
        mock_input = ['2 3', '4 2', '5 7 6']
        expected = '25'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask870ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_870A_acceptance_2(self):
        mock_input = ['8 8', '1 2 3 4 5 6 7 8', '8 7 6 5 4 3 2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask870ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

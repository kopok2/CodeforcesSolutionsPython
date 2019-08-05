import unittest
from unittest.mock import patch

from cdf_730A import CodeforcesTask730ASolution


class TestCDF730A(unittest.TestCase):
    def test_730A_acceptance_1(self):
        mock_input = ['5', '4 5 1 7 4']
        expected = '1\n8\n01010\n00011\n01010\n10010\n00011\n11000\n00011\n11000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask730ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_730A_acceptance_2(self):
        mock_input = ['2', '1 2']
        expected = '0\n2\n11\n11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask730ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_730A_acceptance_3(self):
        mock_input = ['3', '1 1 1']
        expected = '1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask730ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

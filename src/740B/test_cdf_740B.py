import unittest
from unittest.mock import patch

from cdf_740B import CodeforcesTask740BSolution


class TestCDF740B(unittest.TestCase):
    def test_740B_acceptance_1(self):
        mock_input = ['5 4', '1 -2 1 3 -4', '1 2', '4 5', '3 4', '1 4']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask740BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_740B_acceptance_2(self):
        mock_input = ['4 3', '1 2 3 4', '1 3', '2 4', '1 1']
        expected = '16'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask740BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_740B_acceptance_3(self):
        mock_input = ['2 2', '-1 -2', '1 1', '1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask740BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

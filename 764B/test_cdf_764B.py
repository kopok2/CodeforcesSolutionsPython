import unittest
from unittest.mock import patch

from cdf_764B import CodeforcesTask764BSolution


class TestCDF764B(unittest.TestCase):
    def test_764B_acceptance_1(self):
        mock_input = ['7', '4 3 7 6 9 1 2']
        expected = '2 3 9 6 7 1 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask764BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_764B_acceptance_2(self):
        mock_input = ['8', '6 1 4 2 5 6 9 2']
        expected = '2 1 6 2 5 4 9 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask764BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

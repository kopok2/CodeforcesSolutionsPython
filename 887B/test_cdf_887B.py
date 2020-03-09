import unittest
from unittest.mock import patch

from cdf_887B import CodeforcesTask887BSolution


class TestCDF887B(unittest.TestCase):
    def test_887B_acceptance_1(self):
        mock_input = ['3', '0 1 2 3 4 5', '6 7 8 9 0 1', '2 3 4 5 6 7']
        expected = '87'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask887BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_887B_acceptance_2(self):
        mock_input = ['3', '0 1 3 5 6 8', '1 2 4 5 7 8', '2 3 4 6 7 9']
        expected = '98'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask887BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

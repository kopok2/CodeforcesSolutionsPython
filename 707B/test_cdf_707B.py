import unittest
from unittest.mock import patch

from cdf_707B import CodeforcesTask707BSolution


class TestCDF707B(unittest.TestCase):
    def test_707B_acceptance_1(self):
        mock_input = ['5 4 2', '1 2 5', '1 2 3', '2 3 4', '1 4 10', '1 5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask707BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_707B_acceptance_2(self):
        mock_input = ['3 1 1', '1 2 3', '3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask707BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

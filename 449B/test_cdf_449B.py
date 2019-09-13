import unittest
from unittest.mock import patch

from cdf_449B import CodeforcesTask449BSolution


class TestCDF449B(unittest.TestCase):
    def test_449B_acceptance_1(self):
        mock_input = ['5 5 3', '1 2 1', '2 3 2', '1 3 3', '3 4 4', '1 5 5', '3 5', '4 5', '5 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask449BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_449B_acceptance_2(self):
        mock_input = ['2 2 3', '1 2 2', '2 1 3', '2 1', '2 2', '2 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask449BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_574B import CodeforcesTask574BSolution


class TestCDF574B(unittest.TestCase):
    def test_574B_acceptance_1(self):
        mock_input = ['5 6', '1 2', '1 3', '2 3', '2 4', '3 4', '4 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask574BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_574B_acceptance_2(self):
        mock_input = ['7 4', '2 1', '3 6', '5 1', '1 7']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask574BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_658B import CodeforcesTask658BSolution


class TestCDF658B(unittest.TestCase):
    def test_658B_acceptance_1(self):
        mock_input = ['4 2 8', '300 950 500 200', '1 3', '2 4', '2 3', '1 1', '1 2', '2 1', '2 2', '2 3']
        expected = 'NO\nYES\nNO\nYES\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask658BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_658B_acceptance_2(self):
        mock_input = ['6 3 9', '50 20 51 17 99 24', '1 3', '1 4', '1 5', '1 2', '2 4', '2 2', '1 1', '2 4', '2 3']
        expected = 'NO\nYES\nNO\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask658BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

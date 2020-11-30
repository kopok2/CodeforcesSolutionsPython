import unittest
from unittest.mock import patch

from cdf_134B import CodeforcesTask134BSolution


class TestCDF134B(unittest.TestCase):
    def test_134B_acceptance_1(self):
        mock_input = ['5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask134BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_134B_acceptance_2(self):
        mock_input = ['1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask134BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

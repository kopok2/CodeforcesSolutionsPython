import unittest
from unittest.mock import patch

from cdf_518B import CodeforcesTask518BSolution


class TestCDF518B(unittest.TestCase):
    def test_518B_acceptance_1(self):
        mock_input = ['AbC', 'DCbA']
        expected = '3 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_518B_acceptance_2(self):
        mock_input = ['ABC', 'abc']
        expected = '0 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_518B_acceptance_3(self):
        mock_input = ['abacaba', 'AbaCaBA']
        expected = '3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

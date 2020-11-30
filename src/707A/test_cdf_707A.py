import unittest
from unittest.mock import patch

from cdf_707A import CodeforcesTask707ASolution


class TestCDF707A(unittest.TestCase):
    def test_707A_acceptance_1(self):
        mock_input = ['2 2', 'C M', 'Y Y']
        expected = '#Color'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask707ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_707A_acceptance_2(self):
        mock_input = ['3 2', 'W W', 'W W', 'B B']
        expected = '#Black&White'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask707ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_707A_acceptance_3(self):
        mock_input = ['1 1', 'W']
        expected = '#Black&White'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask707ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

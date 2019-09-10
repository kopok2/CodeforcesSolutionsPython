import unittest
from unittest.mock import patch

from cdf_644A import CodeforcesTask644ASolution


class TestCDF644A(unittest.TestCase):
    def test_644A_acceptance_1(self):
        mock_input = ['3 2 2']
        expected = '0 3\n1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask644ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_644A_acceptance_2(self):
        mock_input = ['8 4 3']
        expected = '7 8 3\n0 1 4\n6 0 5\n0 2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask644ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_644A_acceptance_3(self):
        mock_input = ['10 2 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask644ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

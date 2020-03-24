import unittest
from unittest.mock import patch

from cdf_361A import CodeforcesTask361ASolution


class TestCDF361A(unittest.TestCase):
    def test_361A_acceptance_1(self):
        mock_input = ['2 4']
        expected = '1 3\n3 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask361ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_361A_acceptance_2(self):
        mock_input = ['4 7']
        expected = '2 1 0 4\n4 0 2 1\n1 3 3 0\n0 3 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask361ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

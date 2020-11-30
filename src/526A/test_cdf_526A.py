import unittest
from unittest.mock import patch

from cdf_526A import CodeforcesTask526ASolution


class TestCDF526A(unittest.TestCase):
    def test_526A_acceptance_1(self):
        mock_input = ['16', '.**.*..*.***.**.']
        expected = 'yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask526ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_526A_acceptance_2(self):
        mock_input = ['11', '.*.*...*.*.']
        expected = 'no'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask526ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

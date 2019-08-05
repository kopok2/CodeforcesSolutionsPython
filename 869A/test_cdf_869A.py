import unittest
from unittest.mock import patch

from cdf_869A import CodeforcesTask869ASolution


class TestCDF869A(unittest.TestCase):
    def test_869A_acceptance_1(self):
        mock_input = ['3', '1 2 3', '4 5 6']
        expected = 'Karen'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask869ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_869A_acceptance_2(self):
        mock_input = ['5', '2 4 6 8 10', '9 7 5 3 1']
        expected = 'Karen'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask869ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

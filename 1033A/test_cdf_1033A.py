import unittest
from unittest.mock import patch

from cdf_1033A import CodeforcesTask1033ASolution


class TestCDF1033A(unittest.TestCase):
    def test_1033A_acceptance_1(self):
        mock_input = ['8', '4 4', '1 3', '3 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1033ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1033A_acceptance_2(self):
        mock_input = ['8', '4 4', '2 3', '1 6']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1033ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1033A_acceptance_3(self):
        mock_input = ['8', '3 5', '1 2', '6 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1033ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

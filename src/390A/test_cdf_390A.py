import unittest
from unittest.mock import patch

from cdf_390A import CodeforcesTask390ASolution


class TestCDF390A(unittest.TestCase):
    def test_390A_acceptance_1(self):
        mock_input = ['4', '0 0', '0 1', '0 2', '1 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask390ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_390A_acceptance_2(self):
        mock_input = ['4', '0 0', '0 1', '1 0', '1 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask390ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_390A_acceptance_3(self):
        mock_input = ['4', '1 1', '1 2', '2 3', '3 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask390ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

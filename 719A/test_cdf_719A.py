import unittest
from unittest.mock import patch

from cdf_719A import CodeforcesTask719ASolution


class TestCDF719A(unittest.TestCase):
    def test_719A_acceptance_1(self):
        mock_input = ['5', '3 4 5 6 7']
        expected = 'UP'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_719A_acceptance_2(self):
        mock_input = ['7', '12 13 14 15 14 13 12']
        expected = 'DOWN'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_719A_acceptance_3(self):
        mock_input = ['1', '8']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_469A import CodeforcesTask469ASolution


class TestCDF469A(unittest.TestCase):
    def test_469A_acceptance_1(self):
        mock_input = ['4', '3 1 2 3', '2 2 4']
        expected = 'I become the guy.'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask469ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_469A_acceptance_2(self):
        mock_input = ['4', '3 1 2 3', '2 2 3']
        expected = 'Oh, my keyboard!'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask469ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

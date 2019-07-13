import unittest
from unittest.mock import patch

from cdf_786A import CodeforcesTask786ASolution


class TestCDF786A(unittest.TestCase):
    def test_786A_acceptance_1(self):
        mock_input = ['5', '2 3 2', '3 1 2 3']
        expected = 'Lose Win Win Loop\nLoop Win Win Win'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask786ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_786A_acceptance_2(self):
        mock_input = ['8', '4 6 2 3 4', '2 3 6']
        expected = 'Win Win Win Win Win Win Win\nLose Win Lose Lose Win Lose Lose'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask786ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_708A import CodeforcesTask708ASolution


class TestCDF708A(unittest.TestCase):
    def test_708A_acceptance_1(self):
        mock_input = ['codeforces']
        expected = 'bncdenqbdr'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask708ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_708A_acceptance_2(self):
        mock_input = ['abacaba']
        expected = 'aaacaba'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask708ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

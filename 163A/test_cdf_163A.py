import unittest
from unittest.mock import patch

from cdf_163A import CodeforcesTask163ASolution


class TestCDF163A(unittest.TestCase):
    def test_163A_acceptance_1(self):
        mock_input = ['aa', 'aa']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask163ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_163A_acceptance_2(self):
        mock_input = ['codeforces', 'forceofcode']
        expected = '60'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask163ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

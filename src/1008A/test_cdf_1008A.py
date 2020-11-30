import unittest
from unittest.mock import patch

from cdf_1008A import CodeforcesTask1008ASolution


class TestCDF1008A(unittest.TestCase):
    def test_1008A_acceptance_1(self):
        mock_input = ['sumimasen']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1008ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1008A_acceptance_2(self):
        mock_input = ['ninja']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1008ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1008A_acceptance_3(self):
        mock_input = ['codeforces']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1008ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

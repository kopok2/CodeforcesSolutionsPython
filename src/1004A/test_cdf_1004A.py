import unittest
from unittest.mock import patch

from cdf_1004A import CodeforcesTask1004ASolution


class TestCDF1004A(unittest.TestCase):
    def test_1004A_acceptance_1(self):
        mock_input = ['4 3', '-3 2 9 16']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1004ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1004A_acceptance_2(self):
        mock_input = ['5 2', '4 8 11 18 19']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1004ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

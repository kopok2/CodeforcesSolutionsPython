import unittest
from unittest.mock import patch

from cdf_1106B import CodeforcesTask1106BSolution


class TestCDF1106B(unittest.TestCase):
    def test_1106B_acceptance_1(self):
        mock_input = ['8 5 8 6 2 1 4 5 7 5 6 3 3 2 6 2 3 2 2 8 1 4 4 7 3 4 6 10']
        expected = '22 24 14 10 39'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106B_acceptance_2(self):
        mock_input = ['6 6 6 6 6 6 6 6 6 66 666 6666 66666 666666 1 6 2 6 3 6 4 6 5 6 6 66']
        expected = '36 396 3996 39996 399996 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106B_acceptance_3(self):
        mock_input = ['6 6 6 6 6 6 6 6 6 66 666 6666 66666 666666 1 6 2 13 3 6 4 11 5 6 6 6']
        expected = '36 11058 99996 4333326 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

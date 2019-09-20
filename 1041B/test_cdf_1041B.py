import unittest
from unittest.mock import patch

from cdf_1041B import CodeforcesTask1041BSolution


class TestCDF1041B(unittest.TestCase):
    def test_1041B_acceptance_1(self):
        mock_input = ['17 15 5 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1041BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1041B_acceptance_2(self):
        mock_input = ['14 16 7 22']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1041BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1041B_acceptance_3(self):
        mock_input = ['4 2 6 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1041BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1041B_acceptance_4(self):
        mock_input = ['1000000000000000000 1000000000000000000 999999866000004473 999999822000007597']
        expected = '1000000063'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1041BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

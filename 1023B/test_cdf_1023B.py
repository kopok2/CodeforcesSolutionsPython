import unittest
from unittest.mock import patch

from cdf_1023B import CodeforcesTask1023BSolution


class TestCDF1023B(unittest.TestCase):
    def test_1023B_acceptance_1(self):
        mock_input = ['8 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1023BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1023B_acceptance_2(self):
        mock_input = ['8 15']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1023BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1023B_acceptance_3(self):
        mock_input = ['7 20']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1023BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1023B_acceptance_4(self):
        mock_input = ['1000000000000 1000000000001']
        expected = '500000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1023BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1121B import CodeforcesTask1121BSolution


class TestCDF1121B(unittest.TestCase):
    def test_1121B_acceptance_1(self):
        mock_input = ['8\n', '1 8 3 11 4 9 2 7']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1121BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1121B_acceptance_2(self):
        mock_input = ['7\n', '3 1 7 11 9 2 12']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1121BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

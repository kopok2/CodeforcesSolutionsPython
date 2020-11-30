import unittest
from unittest.mock import patch

from cdf_1105B import CodeforcesTask1105BSolution


class TestCDF1105B(unittest.TestCase):
    def test_1105B_acceptance_1(self):
        mock_input = ['8 2 aaacaabb']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1105BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1105B_acceptance_2(self):
        mock_input = ['2 1 ab']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1105BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1105B_acceptance_3(self):
        mock_input = ['4 2 abab']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1105BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

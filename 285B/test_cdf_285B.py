import unittest
from unittest.mock import patch

from cdf_285B import CodeforcesTask285BSolution


class TestCDF285B(unittest.TestCase):
    def test_285B_acceptance_1(self):
        mock_input = ['4 2 1', '2 3 4 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_285B_acceptance_2(self):
        mock_input = ['4 3 3', '4 1 3 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_285B_acceptance_3(self):
        mock_input = ['4 3 4', '1 2 3 4']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_285B_acceptance_4(self):
        mock_input = ['3 1 3', '2 1 3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

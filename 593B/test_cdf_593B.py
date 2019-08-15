import unittest
from unittest.mock import patch

from cdf_593B import CodeforcesTask593BSolution


class TestCDF593B(unittest.TestCase):
    def test_593B_acceptance_1(self):
        mock_input = ['4', '1 2', '1 2', '1 0', '0 1', '0 2']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask593BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_593B_acceptance_2(self):
        mock_input = ['2', '1 3', '1 0', '-1 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask593BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_593B_acceptance_3(self):
        mock_input = ['2', '1 3', '1 0', '0 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask593BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_593B_acceptance_4(self):
        mock_input = ['2', '1 3', '1 0', '0 3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask593BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

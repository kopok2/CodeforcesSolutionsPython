import unittest
from unittest.mock import patch

from cdf_1113B import CodeforcesTask1113BSolution


class TestCDF1113B(unittest.TestCase):
    def test_1113B_acceptance_1(self):
        mock_input = ['5 1 2 3 4 5']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1113BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1113B_acceptance_2(self):
        mock_input = ['4 4 2 4 4']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1113BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1113B_acceptance_3(self):
        mock_input = ['5 2 4 2 3 7']
        expected = '18'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1113BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

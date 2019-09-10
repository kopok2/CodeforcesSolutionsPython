import unittest
from unittest.mock import patch

from cdf_1003B import CodeforcesTask1003BSolution


class TestCDF1003B(unittest.TestCase):
    def test_1003B_acceptance_1(self):
        mock_input = ['2 2 1']
        expected = '1100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1003BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1003B_acceptance_2(self):
        mock_input = ['3 3 3']
        expected = '101100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1003BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1003B_acceptance_3(self):
        mock_input = ['5 3 6']
        expected = '01010100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1003BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

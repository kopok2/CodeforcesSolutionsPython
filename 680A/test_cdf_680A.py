import unittest
from unittest.mock import patch

from cdf_680A import CodeforcesTask680ASolution


class TestCDF680A(unittest.TestCase):
    def test_680A_acceptance_1(self):
        mock_input = ['7 3 7 3 20']
        expected = '26'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask680ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_680A_acceptance_2(self):
        mock_input = ['7 9 3 1 8']
        expected = '28'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask680ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_680A_acceptance_3(self):
        mock_input = ['10 10 10 10 10']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask680ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

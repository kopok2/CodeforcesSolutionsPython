import unittest
from unittest.mock import patch

from cdf_793A import CodeforcesTask793ASolution


class TestCDF793A(unittest.TestCase):
    def test_793A_acceptance_1(self):
        mock_input = ['3 3', '12 9 15']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask793ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_793A_acceptance_2(self):
        mock_input = ['2 2', '10 9']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask793ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_793A_acceptance_3(self):
        mock_input = ['4 1', '1 1000000000 1000000000 1000000000']
        expected = '2999999997'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask793ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

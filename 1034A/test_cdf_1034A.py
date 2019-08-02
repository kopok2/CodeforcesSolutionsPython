import unittest
from unittest.mock import patch

from cdf_1034A import CodeforcesTask1034ASolution


class TestCDF1034A(unittest.TestCase):
    def test_1034A_acceptance_1(self):
        mock_input = ['3', '1 2 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1034ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1034A_acceptance_2(self):
        mock_input = ['4', '6 9 15 30']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1034ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1034A_acceptance_3(self):
        mock_input = ['3', '1 1 1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1034ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_895A import CodeforcesTask895ASolution


class TestCDF895A(unittest.TestCase):
    def test_895A_acceptance_1(self):
        mock_input = ['4', '90 90 90 90']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask895ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_895A_acceptance_2(self):
        mock_input = ['3', '100 100 160']
        expected = '40'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask895ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_895A_acceptance_3(self):
        mock_input = ['1', '360']
        expected = '360'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask895ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_895A_acceptance_4(self):
        mock_input = ['4', '170 30 150 10']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask895ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

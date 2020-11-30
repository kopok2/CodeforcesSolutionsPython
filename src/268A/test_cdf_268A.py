import unittest
from unittest.mock import patch

from cdf_268A import CodeforcesTask268ASolution


class TestCDF268A(unittest.TestCase):
    def test_268A_acceptance_1(self):
        mock_input = ['3', '1 2', '2 4', '3 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask268ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_268A_acceptance_2(self):
        mock_input = ['4', '100 42', '42 100', '5 42', '100 5']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask268ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_268A_acceptance_3(self):
        mock_input = ['2', '1 2', '1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask268ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

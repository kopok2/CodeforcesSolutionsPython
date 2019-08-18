import unittest
from unittest.mock import patch

from cdf_995A import CodeforcesTask995ASolution


class TestCDF995A(unittest.TestCase):
    def test_995A_acceptance_1(self):
        mock_input = ['4 5', '1 2 0 4', '1 2 0 4', '5 0 0 3', '0 5 0 3']
        expected = '6\n1 1 1\n2 1 2\n4 1 4\n3 4 4\n5 3 2\n5 4 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask995ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_995A_acceptance_2(self):
        mock_input = ['1 2', '1', '2', '1', '2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask995ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_995A_acceptance_3(self):
        mock_input = ['1 2', '1', '1', '2', '2']
        expected = '2\n1 1 1\n2 4 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask995ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

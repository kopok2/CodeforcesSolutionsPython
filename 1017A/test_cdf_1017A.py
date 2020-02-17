import unittest
from unittest.mock import patch

from cdf_1017A import CodeforcesTask1017ASolution


class TestCDF1017A(unittest.TestCase):
    def test_1017A_acceptance_1(self):
        mock_input = ['5', '100 98 100 100', '100 100 100 100', '100 100 99 99', '90 99 90 100', '100 98 60 99']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1017ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1017A_acceptance_2(self):
        mock_input = ['6', '100 80 90 99', '60 60 60 60', '90 60 100 60', '60 100 60 80', '100 100 0 100', '0 0 0 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1017ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

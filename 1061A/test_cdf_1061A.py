import unittest
from unittest.mock import patch

from cdf_1061A import CodeforcesTask1061ASolution


class TestCDF1061A(unittest.TestCase):
    def test_1061A_acceptance_1(self):
        mock_input = ['5 11']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1061ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1061A_acceptance_2(self):
        mock_input = ['6 16']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1061ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1037A import CodeforcesTask1037ASolution


class TestCDF1037A(unittest.TestCase):
    def test_1037A_acceptance_1(self):
        mock_input = ['6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1037ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1037A_acceptance_2(self):
        mock_input = ['2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1037ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

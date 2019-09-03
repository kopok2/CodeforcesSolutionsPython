import unittest
from unittest.mock import patch

from cdf_327A import CodeforcesTask327ASolution


class TestCDF327A(unittest.TestCase):
    def test_327A_acceptance_1(self):
        mock_input = ['5', '1 0 0 1 0']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask327ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_327A_acceptance_2(self):
        mock_input = ['4', '1 0 0 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask327ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

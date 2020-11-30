import unittest
from unittest.mock import patch

from cdf_1047A import CodeforcesTask1047ASolution


class TestCDF1047A(unittest.TestCase):
    def test_1047A_acceptance_1(self):
        mock_input = ['3']
        expected = '1 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1047ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1047A_acceptance_2(self):
        mock_input = ['233']
        expected = '77 77 79'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1047ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

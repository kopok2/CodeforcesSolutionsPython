import unittest
from unittest.mock import patch

from cdf_54A import CodeforcesTask54ASolution


class TestCDF54A(unittest.TestCase):
    def test_54A_acceptance_1(self):
        mock_input = ['5 2', '1 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask54ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_54A_acceptance_2(self):
        mock_input = ['10 1', '3 6 7 8']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask54ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

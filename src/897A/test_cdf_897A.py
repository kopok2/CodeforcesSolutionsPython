import unittest
from unittest.mock import patch

from cdf_897A import CodeforcesTask897ASolution


class TestCDF897A(unittest.TestCase):
    def test_897A_acceptance_1(self):
        mock_input = ['3 1', 'ioi', '1 1 i n']
        expected = 'noi'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask897ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_897A_acceptance_2(self):
        mock_input = ['5 3', 'wxhak', '3 3 h x', '1 5 x a', '1 3 w g']
        expected = 'gaaak'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask897ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

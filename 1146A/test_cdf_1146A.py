import unittest
from unittest.mock import patch

from cdf_1146A import CodeforcesTask1146ASolution


class TestCDF1146A(unittest.TestCase):
    def test_1146A_acceptance_1(self):
        mock_input = ['xaxxxxa']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1146ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1146A_acceptance_2(self):
        mock_input = ['aaabaa']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1146ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

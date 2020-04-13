import unittest
from unittest.mock import patch

from cdf_1131A import CodeforcesTask1131ASolution


class TestCDF1131A(unittest.TestCase):
    def test_1131A_acceptance_1(self):
        mock_input = ['2 1 2 1']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1131ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1131A_acceptance_2(self):
        mock_input = ['2 2 1 2']
        expected = '16'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1131ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1030A import CodeforcesTask1030ASolution


class TestCDF1030A(unittest.TestCase):
    def test_1030A_acceptance_1(self):
        mock_input = ['3', '0 0 1']
        expected = 'HARD'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1030ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1030A_acceptance_2(self):
        mock_input = ['1', '0']
        expected = 'EASY'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1030ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

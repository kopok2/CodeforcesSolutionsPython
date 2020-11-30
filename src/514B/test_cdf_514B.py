import unittest
from unittest.mock import patch

from cdf_514B import CodeforcesTask514BSolution


class TestCDF514B(unittest.TestCase):
    def test_514B_acceptance_1(self):
        mock_input = ['4 0 0', '1 1', '2 2', '2 0', '-1 -1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask514BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_514B_acceptance_2(self):
        mock_input = ['2 1 2', '1 1', '1 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask514BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

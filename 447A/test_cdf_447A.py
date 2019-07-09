import unittest
from unittest.mock import patch

from cdf_447A import CodeforcesTask447ASolution


class TestCDF447A(unittest.TestCase):
    def test_447A_acceptance_1(self):
        mock_input = ['10 5', '0', '21', '53', '41', '53']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask447ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_447A_acceptance_2(self):
        mock_input = ['5 5', '0', '1', '2', '3', '4']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask447ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_815A import CodeforcesTask815ASolution


class TestCDF815A(unittest.TestCase):
    def test_815A_acceptance_1(self):
        mock_input = ['3 5', '2 2 2 3 2', '0 0 0 1 0', '1 1 1 2 1']
        expected = '4\nrow 1\nrow 1\ncol 4\nrow 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask815ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_815A_acceptance_2(self):
        mock_input = ['3 3', '0 0 0', '0 1 0', '0 0 0']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask815ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_815A_acceptance_3(self):
        mock_input = ['3 3', '1 1 1', '1 1 1', '1 1 1']
        expected = '3\nrow 1\nrow 2\nrow 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask815ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

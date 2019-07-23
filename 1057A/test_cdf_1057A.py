import unittest
from unittest.mock import patch

from cdf_1057A import CodeforcesTask1057ASolution


class TestCDF1057A(unittest.TestCase):
    def test_1057A_acceptance_1(self):
        mock_input = ['8', '1 1 2 2 3 2 5']
        expected = '1 2 5 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1057A_acceptance_2(self):
        mock_input = ['6', '1 2 3 4 5']
        expected = '1 2 3 4 5 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1057A_acceptance_3(self):
        mock_input = ['7', '1 1 2 3 4 3']
        expected = '1 3 7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1057ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

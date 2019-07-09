import unittest
from unittest.mock import patch

from cdf_1040A import CodeforcesTask1040ASolution


class TestCDF1040A(unittest.TestCase):
    def test_1040A_acceptance_1(self):
        mock_input = ['5 100 1', '0 1 2 1 2']
        expected = '101'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1040ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1040A_acceptance_2(self):
        mock_input = ['3 10 12', '1 2 0']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1040ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1040A_acceptance_3(self):
        mock_input = ['3 12 1', '0 1 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1040ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1059A import CodeforcesTask1059ASolution


class TestCDF1059A(unittest.TestCase):
    def test_1059A_acceptance_1(self):
        mock_input = ['2 11 3', '0 1', '1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1059A_acceptance_2(self):
        mock_input = ['0 5 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1059A_acceptance_3(self):
        mock_input = ['1 3 2', '1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

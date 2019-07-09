import unittest
from unittest.mock import patch

from cdf_1133A import CodeforcesTask1133ASolution


class TestCDF1133A(unittest.TestCase):
    def test_1133A_acceptance_1(self):
        mock_input = ['10:00 11:00']
        expected = '10:30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1133ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1133A_acceptance_2(self):
        mock_input = ['11:10 11:12']
        expected = '11:11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1133ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1133A_acceptance_3(self):
        mock_input = ['01:02 03:02']
        expected = '02:02'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1133ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1010A import CodeforcesTask1010ASolution


class TestCDF1010A(unittest.TestCase):
    def test_1010A_acceptance_1(self):
        mock_input = ['2', '12', '11 8', '7 5']
        expected = '10.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1010ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1010A_acceptance_2(self):
        mock_input = ['3', '1', '1 4 1', '2 5 3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1010ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1010A_acceptance_3(self):
        mock_input = ['6', '2', '4 6 3 3 5 6', '2 6 3 6 5 3']
        expected = '85.4800000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1010ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

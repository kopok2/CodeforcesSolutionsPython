import unittest
from unittest.mock import patch

from cdf_531A import CodeforcesTask531ASolution


class TestCDF531A(unittest.TestCase):
    def test_531A_acceptance_1(self):
        mock_input = ['1 -2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask531ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_531A_acceptance_2(self):
        mock_input = ['1 0 -1']
        expected = '-1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask531ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_531A_acceptance_3(self):
        mock_input = ['2 -3 1']
        expected = '0.5 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask531ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

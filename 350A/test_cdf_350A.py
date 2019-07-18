import unittest
from unittest.mock import patch

from cdf_350A import CodeforcesTask350ASolution


class TestCDF350A(unittest.TestCase):
    def test_350A_acceptance_1(self):
        mock_input = ['3 6', '4 5 2', '8 9 6 10 7 11']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask350ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_350A_acceptance_2(self):
        mock_input = ['3 1', '3 4 5', '6']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask350ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

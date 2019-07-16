import unittest
from unittest.mock import patch

from cdf_336A import CodeforcesTask336ASolution


class TestCDF336A(unittest.TestCase):
    def test_336A_acceptance_1(self):
        mock_input = ['10 5']
        expected = '0 15 15 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask336ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_336A_acceptance_2(self):
        mock_input = ['-10 5']
        expected = '-15 0 0 15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask336ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

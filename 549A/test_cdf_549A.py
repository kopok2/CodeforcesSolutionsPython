import unittest
from unittest.mock import patch

from cdf_549A import CodeforcesTask549ASolution


class TestCDF549A(unittest.TestCase):
    def test_549A_acceptance_1(self):
        mock_input = ['4 4', 'xxxx', 'xfax', 'xcex', 'xxxx']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask549ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_549A_acceptance_2(self):
        mock_input = ['4 2', 'xx', 'cf', 'ae', 'xx']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask549ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_549A_acceptance_3(self):
        mock_input = ['2 3', 'fac', 'cef']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask549ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_549A_acceptance_4(self):
        mock_input = ['1 4', 'face']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask549ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

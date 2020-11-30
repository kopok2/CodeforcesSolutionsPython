import unittest
from unittest.mock import patch

from cdf_950A import CodeforcesTask950ASolution


class TestCDF950A(unittest.TestCase):
    def test_950A_acceptance_1(self):
        mock_input = ['1 4 2']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask950ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_950A_acceptance_2(self):
        mock_input = ['5 5 5']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask950ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_950A_acceptance_3(self):
        mock_input = ['0 2 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask950ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

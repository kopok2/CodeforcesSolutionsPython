import unittest
from unittest.mock import patch
from random import randrange

from cdf_930A import CodeforcesTask930ASolution


class TestCDF930A(unittest.TestCase):
    def test_930A_acceptance_1(self):
        mock_input = ['3', '1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask930ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_930A_acceptance_2(self):
        mock_input = ['5', '1 2 2 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask930ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_930A_acceptance_3(self):
        mock_input = ['18', '1 1 1 4 4 3 2 2 2 10 8 9 9 9 10 10 4']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask930ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_930A_acceptance_4(self):
        mock_input = ['1000000', ' '.join([str(x + 1) for x in range(999999)])]
        expected = '1000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask930ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

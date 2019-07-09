import unittest
from unittest.mock import patch

from cdf_190A import CodeforcesTask190ASolution


class TestCDF190A(unittest.TestCase):
    def test_190A_acceptance_1(self):
        mock_input = ['1 2']
        expected = '2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask190ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_190A_acceptance_2(self):
        mock_input = ['0 5']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask190ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_190A_acceptance_3(self):
        mock_input = ['2 2']
        expected = '2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask190ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

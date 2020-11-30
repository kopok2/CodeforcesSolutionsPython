import unittest
from unittest.mock import patch

from cdf_150A import CodeforcesTask150ASolution


class TestCDF150A(unittest.TestCase):
    def test_150A_acceptance_1(self):
        mock_input = ['6']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask150ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_150A_acceptance_2(self):
        mock_input = ['30']
        expected = '1\n6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask150ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_150A_acceptance_3(self):
        mock_input = ['1']
        expected = '1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask150ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

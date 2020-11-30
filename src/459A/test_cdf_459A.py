import unittest
from unittest.mock import patch

from cdf_459A import CodeforcesTask459ASolution


class TestCDF459A(unittest.TestCase):
    def test_459A_acceptance_1(self):
        mock_input = ['0 0 0 1']
        expected = '1 0 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_459A_acceptance_2(self):
        mock_input = ['0 0 1 1']
        expected = '0 1 1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_459A_acceptance_3(self):
        mock_input = ['0 0 1 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

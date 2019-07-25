import unittest
from unittest.mock import patch

from cdf_643A import CodeforcesTask643ASolution


class TestCDF643A(unittest.TestCase):
    def test_643A_acceptance_1(self):
        mock_input = ['4', '1 2 1 2']
        expected = '7 3 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask643ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_643A_acceptance_2(self):
        mock_input = ['3', '1 1 1']
        expected = '6 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask643ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

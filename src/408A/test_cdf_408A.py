import unittest
from unittest.mock import patch

from cdf_408A import CodeforcesTask408ASolution


class TestCDF408A(unittest.TestCase):
    def test_408A_acceptance_1(self):
        mock_input = ['1', '1', '1']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask408ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_408A_acceptance_2(self):
        mock_input = ['4', '1 4 3 2', '100', '1 2 2 3', '1 9 1', '7 8']
        expected = '100'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask408ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

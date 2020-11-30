import unittest
from unittest.mock import patch

from cdf_873A import CodeforcesTask873ASolution


class TestCDF873A(unittest.TestCase):
    def test_873A_acceptance_1(self):
        mock_input = ['4 2 2', '3 6 7 10']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask873ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_873A_acceptance_2(self):
        mock_input = ['5 2 1', '100 100 100 100 100']
        expected = '302'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask873ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_499A import CodeforcesTask499ASolution


class TestCDF499A(unittest.TestCase):
    def test_499A_acceptance_1(self):
        mock_input = ['2 3', '5 6', '10 12']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask499ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_499A_acceptance_2(self):
        mock_input = ['1 1', '1 100000']
        expected = '100000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask499ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_10A import CodeforcesTask10ASolution


class TestCDF10A(unittest.TestCase):
    def test_10A_acceptance_1(self):
        mock_input = ['1 3 2 1 5 10', '0 10']
        expected = '30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask10ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_10A_acceptance_2(self):
        mock_input = ['2 8 4 2 5 10', '20 30', '50 100']
        expected = '570'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask10ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

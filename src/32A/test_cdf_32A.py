import unittest
from unittest.mock import patch

from cdf_32A import CodeforcesTask32ASolution


class TestCDF32A(unittest.TestCase):
    def test_32A_acceptance_1(self):
        mock_input = ['5 10', '10 20 50 60 65']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask32ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_32A_acceptance_2(self):
        mock_input = ['5 1', '55 30 29 31 55']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask32ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

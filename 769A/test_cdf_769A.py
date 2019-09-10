import unittest
from unittest.mock import patch

from cdf_769A import CodeforcesTask769ASolution


class TestCDF769A(unittest.TestCase):
    def test_769A_acceptance_1(self):
        mock_input = ['3', '2014 2016 2015']
        expected = '2015'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask769ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_769A_acceptance_2(self):
        mock_input = ['1', '2050']
        expected = '2050'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask769ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

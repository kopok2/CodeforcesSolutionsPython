import unittest
from unittest.mock import patch

from cdf_173A import CodeforcesTask173ASolution


class TestCDF173A(unittest.TestCase):
    def test_173A_acceptance_1(self):
        mock_input = ['7', 'RPS', 'RSPP']
        expected = '3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask173ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_173A_acceptance_2(self):
        mock_input = ['5', 'RRRRRRRR', 'R']
        expected = '0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask173ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

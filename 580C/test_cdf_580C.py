import unittest
from unittest.mock import patch

from cdf_580C import CodeforcesTask580CSolution


class TestCDF580C(unittest.TestCase):
    def test_580C_acceptance_1(self):
        mock_input = ['4 1', '1 1 0 0', '1 2', '1 3', '1 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask580CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_580C_acceptance_2(self):
        mock_input = ['7 1', '1 0 1 1 0 0 0', '1 2', '1 3', '2 4', '2 5', '3 6', '3 7']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask580CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

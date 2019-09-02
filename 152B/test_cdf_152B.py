import unittest
from unittest.mock import patch

from cdf_152B import CodeforcesTask152BSolution


class TestCDF152B(unittest.TestCase):
    def test_152B_acceptance_1(self):
        mock_input = ['4 5', '1 1', '3', '1 1', '1 1', '0 -2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask152BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_152B_acceptance_2(self):
        mock_input = ['10 10', '1 2', '1', '-1 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask152BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

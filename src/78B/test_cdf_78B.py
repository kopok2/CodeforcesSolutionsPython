import unittest
from unittest.mock import patch

from cdf_78B import CodeforcesTask78BSolution


class TestCDF78B(unittest.TestCase):
    def test_78B_acceptance_1(self):
        mock_input = ['8']
        expected = 'ROYGRBIV'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask78BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_78B_acceptance_2(self):
        mock_input = ['13']
        expected = 'ROYGBIVGBIVYG'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask78BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

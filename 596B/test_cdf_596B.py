import unittest
from unittest.mock import patch

from cdf_596B import CodeforcesTask596BSolution


class TestCDF596B(unittest.TestCase):
    def test_596B_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask596BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_596B_acceptance_2(self):
        mock_input = ['4', '1 2 2 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask596BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

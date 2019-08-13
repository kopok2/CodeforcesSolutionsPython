import unittest
from unittest.mock import patch

from cdf_602B import CodeforcesTask602BSolution


class TestCDF602B(unittest.TestCase):
    def test_602B_acceptance_1(self):
        mock_input = ['5', '1 2 3 3 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask602BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_602B_acceptance_2(self):
        mock_input = ['11', '5 4 5 5 6 7 8 8 8 7 6']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask602BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

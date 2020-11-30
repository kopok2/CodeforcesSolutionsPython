import unittest
from unittest.mock import patch

from cdf_69B import CodeforcesTask69BSolution


class TestCDF69B(unittest.TestCase):
    def test_69B_acceptance_1(self):
        mock_input = ['4 4', '1 4 20 5', '1 3 21 10', '3 3 4 30', '3 4 4 20']
        expected = '60'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask69BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_69B_acceptance_2(self):
        mock_input = ['8 4', '1 5 24 10', '2 4 6 15', '4 6 30 50', '6 7 4 20']
        expected = '105'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask69BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

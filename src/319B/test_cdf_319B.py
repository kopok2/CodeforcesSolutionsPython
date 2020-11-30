import unittest
from unittest.mock import patch

from cdf_319B import CodeforcesTask319BSolution


class TestCDF319B(unittest.TestCase):
    def test_319B_acceptance_1(self):
        mock_input = ['10', '10 9 7 8 6 5 3 4 2 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask319BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_319B_acceptance_2(self):
        mock_input = ['6', '1 2 3 4 5 6']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask319BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

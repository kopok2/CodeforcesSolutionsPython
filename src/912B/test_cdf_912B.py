import unittest
from unittest.mock import patch

from cdf_912B import CodeforcesTask912BSolution


class TestCDF912B(unittest.TestCase):
    def test_912B_acceptance_1(self):
        mock_input = ['4 3']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask912BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_912B_acceptance_2(self):
        mock_input = ['6 6']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask912BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_475B import CodeforcesTask475BSolution


class TestCDF475B(unittest.TestCase):
    def test_475B_acceptance_1(self):
        mock_input = ['3 3', '><>', 'v^v']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask475BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_475B_acceptance_2(self):
        mock_input = ['4 6', '<><>', 'v^v^v^']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask475BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

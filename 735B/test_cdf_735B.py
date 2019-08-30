import unittest
from unittest.mock import patch

from cdf_735B import CodeforcesTask735BSolution


class TestCDF735B(unittest.TestCase):
    def test_735B_acceptance_1(self):
        mock_input = ['2 1 1', '1 5']
        expected = '6.00000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask735BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_735B_acceptance_2(self):
        mock_input = ['4 2 1', '1 4 2 3']
        expected = '6.50000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask735BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

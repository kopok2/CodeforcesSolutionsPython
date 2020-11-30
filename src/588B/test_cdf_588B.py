import unittest
from unittest.mock import patch

from cdf_588B import CodeforcesTask588BSolution


class TestCDF588B(unittest.TestCase):
    def test_588B_acceptance_1(self):
        mock_input = ['10']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask588BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_588B_acceptance_2(self):
        mock_input = ['12']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask588BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

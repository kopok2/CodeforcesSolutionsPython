import unittest
from unittest.mock import patch

from cdf_289B import CodeforcesTask289BSolution


class TestCDF289B(unittest.TestCase):
    def test_289B_acceptance_1(self):
        mock_input = ['2 2 2', '2 4', '6 8']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask289BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_289B_acceptance_2(self):
        mock_input = ['1 2 7', '6 7']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask289BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

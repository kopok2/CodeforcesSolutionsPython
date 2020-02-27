import unittest
from unittest.mock import patch

from cdf_597B import CodeforcesTask597BSolution


class TestCDF597B(unittest.TestCase):
    def test_597B_acceptance_1(self):
        mock_input = ['2', '7 11', '4 7']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask597BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_597B_acceptance_2(self):
        mock_input = ['5', '1 2', '2 3', '3 4', '4 5', '5 6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask597BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_597B_acceptance_3(self):
        mock_input = ['6', '4 8', '1 5', '4 7', '2 5', '1 3', '6 8']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask597BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

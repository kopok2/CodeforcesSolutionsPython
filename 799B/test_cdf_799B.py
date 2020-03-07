import unittest
from unittest.mock import patch

from cdf_799B import CodeforcesTask799BSolution


class TestCDF799B(unittest.TestCase):
    def test_799B_acceptance_1(self):
        mock_input = ['5', '300 200 400 500 911', '1 2 1 2 3', '2 1 3 2 1', '6', '2 3 1 2 1 1']
        expected = '200 400 300 500 911 -1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask799BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_799B_acceptance_2(self):
        mock_input = ['2', '1000000000 1', '1 1', '1 2', '2', '2 1']
        expected = '1 1000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask799BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

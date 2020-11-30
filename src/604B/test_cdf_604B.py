import unittest
from unittest.mock import patch

from cdf_604B import CodeforcesTask604BSolution


class TestCDF604B(unittest.TestCase):
    def test_604B_acceptance_1(self):
        mock_input = ['2 1', '2 5']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask604BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_604B_acceptance_2(self):
        mock_input = ['4 3', '2 3 5 9']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask604BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_604B_acceptance_3(self):
        mock_input = ['3 2', '3 5 7']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask604BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

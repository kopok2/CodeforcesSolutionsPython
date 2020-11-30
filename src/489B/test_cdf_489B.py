import unittest
from unittest.mock import patch

from cdf_489B import CodeforcesTask489BSolution


class TestCDF489B(unittest.TestCase):
    def test_489B_acceptance_1(self):
        mock_input = ['4', '1 4 6 2', '5', '5 1 5 7 9']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask489BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_489B_acceptance_2(self):
        mock_input = ['4', '1 2 3 4', '4', '10 11 12 13']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask489BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_489B_acceptance_3(self):
        mock_input = ['5', '1 1 1 1 1', '3', '1 2 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask489BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

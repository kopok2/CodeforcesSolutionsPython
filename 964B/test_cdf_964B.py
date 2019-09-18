import unittest
from unittest.mock import patch

from cdf_964B import CodeforcesTask964BSolution


class TestCDF964B(unittest.TestCase):
    def test_964B_acceptance_1(self):
        mock_input = ['4 5 5 3 5', '1 5 5 4']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask964BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_964B_acceptance_2(self):
        mock_input = ['5 3 1 1 3', '2 2 2 1 1']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask964BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_964B_acceptance_3(self):
        mock_input = ['5 5 3 4 5', '1 2 3 4 5']
        expected = '35'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask964BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

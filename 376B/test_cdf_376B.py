import unittest
from unittest.mock import patch

from cdf_376B import CodeforcesTask376BSolution


class TestCDF376B(unittest.TestCase):
    def test_376B_acceptance_1(self):
        mock_input = ['5 3', '1 2 10', '2 3 1', '2 4 1']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask376BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_376B_acceptance_2(self):
        mock_input = ['3 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask376BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_376B_acceptance_3(self):
        mock_input = ['4 3', '1 2 1', '2 3 1', '3 1 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask376BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

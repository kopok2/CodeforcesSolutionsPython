import unittest
from unittest.mock import patch

from cdf_415B import CodeforcesTask415BSolution


class TestCDF415B(unittest.TestCase):
    def test_415B_acceptance_1(self):
        mock_input = ['5 1 4', '12 6 11 9 1']
        expected = '0 2 3 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask415BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_415B_acceptance_2(self):
        mock_input = ['3 1 2', '1 2 3']
        expected = '1 0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask415BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_415B_acceptance_3(self):
        mock_input = ['1 1 1', '1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask415BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

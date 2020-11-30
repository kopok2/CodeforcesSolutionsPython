import unittest
from unittest.mock import patch

from cdf_808B import CodeforcesTask808BSolution


class TestCDF808B(unittest.TestCase):
    def test_808B_acceptance_1(self):
        mock_input = ['3 2', '3 4 7']
        expected = '9.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask808BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_808B_acceptance_2(self):
        mock_input = ['1 1', '10']
        expected = '10.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask808BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_808B_acceptance_3(self):
        mock_input = ['8 2', '1 2 4 100000 123 456 789 1']
        expected = '28964.2857142857'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask808BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

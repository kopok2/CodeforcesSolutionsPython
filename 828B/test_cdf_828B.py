import unittest
from unittest.mock import patch

from cdf_828B import CodeforcesTask828BSolution


class TestCDF828B(unittest.TestCase):
    def test_828B_acceptance_1(self):
        mock_input = ['5 4', 'WWWW', 'WWWB', 'WWWB', 'WWBB', 'WWWW']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask828BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_828B_acceptance_2(self):
        mock_input = ['1 2', 'BB']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask828BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_828B_acceptance_3(self):
        mock_input = ['3 3', 'WWW', 'WWW', 'WWW']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask828BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

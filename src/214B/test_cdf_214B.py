import unittest
from unittest.mock import patch

from cdf_214B import CodeforcesTask214BSolution


class TestCDF214B(unittest.TestCase):
    def test_214B_acceptance_1(self):
        mock_input = ['1', '0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask214BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_214B_acceptance_2(self):
        mock_input = ['11', '3 4 5 4 5 3 5 3 4 4 0']
        expected = '5554443330'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask214BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_214B_acceptance_3(self):
        mock_input = ['8', '3 2 5 1 5 2 2 3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask214BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

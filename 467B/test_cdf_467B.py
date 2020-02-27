import unittest
from unittest.mock import patch

from cdf_467B import CodeforcesTask467BSolution


class TestCDF467B(unittest.TestCase):
    def test_467B_acceptance_1(self):
        mock_input = ['7 3 1', '8', '5', '111', '17']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask467BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_467B_acceptance_2(self):
        mock_input = ['3 3 3', '1', '2', '3', '4']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask467BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

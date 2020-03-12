import unittest
from unittest.mock import patch

from cdf_390B import CodeforcesTask390BSolution


class TestCDF390B(unittest.TestCase):
    def test_390B_acceptance_1(self):
        mock_input = ['3', '1 1 2', '2 2 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask390BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_390B_acceptance_2(self):
        mock_input = ['1', '2', '5']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask390BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

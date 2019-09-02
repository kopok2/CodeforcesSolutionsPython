import unittest
from unittest.mock import patch

from cdf_733B import CodeforcesTask733BSolution


class TestCDF733B(unittest.TestCase):
    def test_733B_acceptance_1(self):
        mock_input = ['3', '5 6', '8 9', '10 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask733BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_733B_acceptance_2(self):
        mock_input = ['2', '6 5', '5 6']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask733BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_733B_acceptance_3(self):
        mock_input = ['6', '5 9', '1 3', '4 8', '4 5', '23 54', '12 32']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask733BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

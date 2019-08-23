import unittest
from unittest.mock import patch

from cdf_789B import CodeforcesTask789BSolution


class TestCDF789B(unittest.TestCase):
    def test_789B_acceptance_1(self):
        mock_input = ['3 2 30 4', '6 14 25 48']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask789BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_789B_acceptance_2(self):
        mock_input = ['123 1 2143435 4', '123 11 -5453 141245']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask789BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_789B_acceptance_3(self):
        mock_input = ['123 1 2143435 4', '54343 -13 6 124']
        expected = 'inf'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask789BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

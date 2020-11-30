import unittest
from unittest.mock import patch

from cdf_172B import CodeforcesTask172BSolution


class TestCDF172B(unittest.TestCase):
    def test_172B_acceptance_1(self):
        mock_input = ['2 6 12 11']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask172BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_172B_acceptance_2(self):
        mock_input = ['2 3 5 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask172BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_172B_acceptance_3(self):
        mock_input = ['3 6 81 9']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask172BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

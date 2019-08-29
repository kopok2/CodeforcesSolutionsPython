import unittest
from unittest.mock import patch

from cdf_1058B import CodeforcesTask1058BSolution


class TestCDF1058B(unittest.TestCase):
    def test_1058B_acceptance_1(self):
        mock_input = ['7 2', '4', '2 4', '4 1', '6 3', '4 5']
        expected = 'YES\nNO\nNO\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1058BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1058B_acceptance_2(self):
        mock_input = ['8 7', '4', '4 4', '2 8', '8 1', '6 1']
        expected = 'YES\nNO\nYES\nYES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1058BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

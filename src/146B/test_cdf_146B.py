import unittest
from unittest.mock import patch

from cdf_146B import CodeforcesTask146BSolution


class TestCDF146B(unittest.TestCase):
    def test_146B_acceptance_1(self):
        mock_input = ['1 7']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask146BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_146B_acceptance_2(self):
        mock_input = ['100 47']
        expected = '147'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask146BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

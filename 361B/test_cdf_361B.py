import unittest
from unittest.mock import patch

from cdf_361B import CodeforcesTask361BSolution


class TestCDF361B(unittest.TestCase):
    def test_361B_acceptance_1(self):
        mock_input = ['4 2']
        expected = '2 4 3 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask361BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_361B_acceptance_2(self):
        mock_input = ['1 1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask361BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

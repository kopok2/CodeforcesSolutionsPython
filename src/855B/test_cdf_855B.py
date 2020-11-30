import unittest
from unittest.mock import patch

from cdf_855B import CodeforcesTask855BSolution


class TestCDF855B(unittest.TestCase):
    def test_855B_acceptance_1(self):
        mock_input = ['5 1 2 3', '1 2 3 4 5']
        expected = '30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask855BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_855B_acceptance_2(self):
        mock_input = ['5 1 2 -3', '-1 -2 -3 -4 -5']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask855BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_609B import CodeforcesTask609BSolution


class TestCDF609B(unittest.TestCase):
    def test_609B_acceptance_1(self):
        mock_input = ['4 3', '2 1 3 1']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask609BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_609B_acceptance_2(self):
        mock_input = ['7 4', '4 2 3 1 2 4 3']
        expected = '18'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask609BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

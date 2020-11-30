import unittest
from unittest.mock import patch

from cdf_339B import CodeforcesTask339BSolution


class TestCDF339B(unittest.TestCase):
    def test_339B_acceptance_1(self):
        mock_input = ['4 3', '3 2 3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask339BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_339B_acceptance_2(self):
        mock_input = ['4 3', '2 3 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask339BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

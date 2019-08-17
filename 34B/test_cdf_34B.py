import unittest
from unittest.mock import patch

from cdf_34B import CodeforcesTask34BSolution


class TestCDF34B(unittest.TestCase):
    def test_34B_acceptance_1(self):
        mock_input = ['5 3', '-6 0 35 -2 4']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask34BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_34B_acceptance_2(self):
        mock_input = ['4 2', '7 0 0 -7']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask34BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

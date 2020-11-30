import unittest
from unittest.mock import patch

from cdf_994A import CodeforcesTask994ASolution


class TestCDF3B(unittest.TestCase):
    def test_994A_acceptance_1(self):
        mock_input = ['7 3', '3 5 7 1 6 2 8', '1 2 7']
        expected = '7 1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask994ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_994A_acceptance_2(self):
        mock_input = ['4 4', '3 4 1 0', '0 1 7 9']
        expected = '1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask994ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

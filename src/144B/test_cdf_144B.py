import unittest
from unittest.mock import patch

from cdf_144B import CodeforcesTask144BSolution


class TestCDF144B(unittest.TestCase):
    def test_144B_acceptance_1(self):
        mock_input = ['2 5 4 2', '3', '3 1 2', '5 3 1', '1 3 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask144BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_144B_acceptance_2(self):
        mock_input = ['5 2 6 3', '2', '6 2 2', '6 5 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask144BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

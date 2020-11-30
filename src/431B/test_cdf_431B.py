import unittest
from unittest.mock import patch

from cdf_431B import CodeforcesTask431BSolution


class TestCDF431B(unittest.TestCase):
    def test_431B_acceptance_1(self):
        mock_input = ['0 0 0 0 9', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 0 0', '7 0 0 0 0']
        expected = '32'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask431BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_431B_acceptance_2(self):
        mock_input = ['0 43 21 18 2', '3 0 21 11 65', '5 2 0 1 4', '54 62 12 0 99', '87 64 81 33 0']
        expected = '620'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask431BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

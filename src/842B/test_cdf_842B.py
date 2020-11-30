import unittest
from unittest.mock import patch

from cdf_842B import CodeforcesTask842BSolution


class TestCDF842B(unittest.TestCase):
    def test_842B_acceptance_1(self):
        mock_input = ['8 4', '7', '7 8 1', '-7 3 2', '0 2 1', '0 -2 2', '-3 -3 1', '0 6 2', '5 3 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask842BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_842B_acceptance_2(self):
        mock_input = ['10 8', '4', '0 0 9', '0 0 10', '1 0 1', '1 0 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask842BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

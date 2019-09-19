import unittest
from unittest.mock import patch

from cdf_680B import CodeforcesTask680BSolution


class TestCDF680B(unittest.TestCase):
    def test_680B_acceptance_1(self):
        mock_input = ['6 3', '1 1 1 0 1 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask680BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_680B_acceptance_2(self):
        mock_input = ['5 2', '0 0 0 1 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask680BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

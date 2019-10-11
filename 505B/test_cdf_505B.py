import unittest
from unittest.mock import patch

from cdf_505B import CodeforcesTask505BSolution


class TestCDF505B(unittest.TestCase):
    def test_505B_acceptance_1(self):
        mock_input = ['4 5', '1 2 1', '1 2 2', '2 3 1', '2 3 3', '2 4 3', '3', '1 2', '3 4', '1 4']
        expected = '2\n1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask505BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_505B_acceptance_2(self):
        mock_input = ['5 7', '1 5 1', '2 5 1', '3 5 1', '4 5 1', '1 2 2', '2 3 2', '3 4 2', '5', '1 5', '5 1', '2 5', '1 5', '1 4']
        expected = '1\n1\n1\n1\n2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask505BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

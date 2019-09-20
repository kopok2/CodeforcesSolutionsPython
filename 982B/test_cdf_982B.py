import unittest
from unittest.mock import patch

from cdf_982B import CodeforcesTask982BSolution


class TestCDF982B(unittest.TestCase):
    def test_982B_acceptance_1(self):
        mock_input = ['2', '3 1', '0011']
        expected = '2 1 1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask982BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_982B_acceptance_2(self):
        mock_input = ['6', '10 8 9 11 13 5', '010010011101']
        expected = '6 6 2 3 3 1 4 4 1 2 5 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask982BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

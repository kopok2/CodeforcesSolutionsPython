import unittest
from unittest.mock import patch

from cdf_292B import CodeforcesTask292BSolution


class TestCDF292B(unittest.TestCase):
    def test_292B_acceptance_1(self):
        mock_input = ['4 3', '1 2', '2 3', '3 4']
        expected = 'bus topology'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask292BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_292B_acceptance_2(self):
        mock_input = ['4 4', '1 2', '2 3', '3 4', '4 1']
        expected = 'ring topology'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask292BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_292B_acceptance_3(self):
        mock_input = ['4 3', '1 2', '1 3', '1 4']
        expected = 'star topology'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask292BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_292B_acceptance_4(self):
        mock_input = ['4 4', '1 2', '2 3', '3 1', '1 4']
        expected = 'unknown topology'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask292BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

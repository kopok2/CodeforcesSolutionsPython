import unittest
from unittest.mock import patch

from cdf_135B import CodeforcesTask135BSolution


class TestCDF135B(unittest.TestCase):
    def test_135B_acceptance_1(self):
        mock_input = ['0 0', '10 11', '10 0', '0 11', '1 1', '2 2', '2 1', '1 2']
        expected = 'YES\n5 6 7 8\n1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask135BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_135B_acceptance_2(self):
        mock_input = ['0 0', '1 1', '2 2', '3 3', '4 4', '5 5', '6 6', '7 7']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask135BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_135B_acceptance_3(self):
        mock_input = ['0 0', '4 4', '4 0', '0 4', '1 2', '2 3', '3 2', '2 1']
        expected = 'YES\n1 2 3 4\n5 6 7 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask135BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_771A import CodeforcesTask771ASolution


class TestCDF771A(unittest.TestCase):
    def test_771A_acceptance_1(self):
        mock_input = ['4 3', '1 3', '3 4', '1 4']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask771ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_771A_acceptance_2(self):
        mock_input = ['4 4', '3 1', '2 3', '3 4', '1 2']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask771ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_771A_acceptance_3(self):
        mock_input = ['10 4', '4 3', '5 10', '8 9', '1 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask771ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_771A_acceptance_4(self):
        mock_input = ['3 2', '1 2', '2 3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask771ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

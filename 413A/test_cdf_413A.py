import unittest
from unittest.mock import patch

from cdf_413A import CodeforcesTask413ASolution


class TestCDF413A(unittest.TestCase):
    def test_413A_acceptance_1(self):
        mock_input = ['2 1 1 2', '1']
        expected = 'Correct'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask413ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_413A_acceptance_2(self):
        mock_input = ['3 1 1 3', '2']
        expected = 'Correct'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask413ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_413A_acceptance_3(self):
        mock_input = ['2 1 1 3', '2']
        expected = 'Incorrect'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask413ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

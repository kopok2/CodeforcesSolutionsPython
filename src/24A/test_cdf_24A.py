import unittest
from unittest.mock import patch

from cdf_24A import CodeforcesTask24ASolution


class TestCDF24A(unittest.TestCase):
    def test_24A_acceptance_1(self):
        mock_input = ['3', '1 3 1', '1 2 1', '3 2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask24ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_24A_acceptance_2(self):
        mock_input = ['3', '1 3 1', '1 2 5', '3 2 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask24ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_24A_acceptance_3(self):
        mock_input = ['6', '1 5 4', '5 3 8', '2 4 15', '1 6 16', '2 3 23', '4 6 42']
        expected = '39'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask24ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_24A_acceptance_4(self):
        mock_input = ['4', '1 2 9', '2 3 8', '3 4 7', '4 1 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask24ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

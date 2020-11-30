import unittest
from unittest.mock import patch

from cdf_601A import CodeforcesTask601ASolution


class TestCDF601A(unittest.TestCase):
    def test_601A_acceptance_1(self):
        mock_input = ['4 2', '1 3', '3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask601ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_601A_acceptance_2(self):
        mock_input = ['4 6', '1 2', '1 3', '1 4', '2 3', '2 4', '3 4']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask601ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_601A_acceptance_3(self):
        mock_input = ['5 5', '4 2', '3 5', '4 5', '5 1', '1 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask601ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

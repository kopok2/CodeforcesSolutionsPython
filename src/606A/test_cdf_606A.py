import unittest
from unittest.mock import patch

from cdf_606A import CodeforcesTask606ASolution


class TestCDF606A(unittest.TestCase):
    def test_606A_acceptance_1(self):
        mock_input = ['4 4 0', '2 1 2']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask606ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_606A_acceptance_2(self):
        mock_input = ['5 6 1', '2 7 2']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask606ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_606A_acceptance_3(self):
        mock_input = ['3 3 3', '2 2 2']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask606ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

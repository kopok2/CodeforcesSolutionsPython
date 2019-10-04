import unittest
from unittest.mock import patch

from cdf_620A import CodeforcesTask620ASolution


class TestCDF620A(unittest.TestCase):
    def test_620A_acceptance_1(self):
        mock_input = ['0 0', '4 5']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask620ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_620A_acceptance_2(self):
        mock_input = ['3 4', '6 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask620ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_551A import CodeforcesTask551ASolution


class TestCDF551A(unittest.TestCase):
    def test_551A_acceptance_1(self):
        mock_input = ['3', '1 3 3']
        expected = '3 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_551A_acceptance_2(self):
        mock_input = ['1', '1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_551A_acceptance_3(self):
        mock_input = ['5', '3 5 3 4 5']
        expected = '4 1 4 3 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask551ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

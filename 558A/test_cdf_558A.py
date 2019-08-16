import unittest
from unittest.mock import patch

from cdf_558A import CodeforcesTask558ASolution


class TestCDF558A(unittest.TestCase):
    def test_558A_acceptance_1(self):
        mock_input = ['2', '-1 5', '1 5']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_558A_acceptance_2(self):
        mock_input = ['3', '-2 2', '1 4', '-1 3']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_558A_acceptance_3(self):
        mock_input = ['3', '1 9', '3 5', '7 10']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

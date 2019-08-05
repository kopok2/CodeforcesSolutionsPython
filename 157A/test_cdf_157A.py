import unittest
from unittest.mock import patch

from cdf_157A import CodeforcesTask157ASolution


class TestCDF157A(unittest.TestCase):
    def test_157A_acceptance_1(self):
        mock_input = ['1', '1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask157ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_157A_acceptance_2(self):
        mock_input = ['2', '1 2', '3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask157ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_157A_acceptance_3(self):
        mock_input = ['4', '5 7 8 4', '9 5 3 2', '1 6 6 4', '9 5 7 3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask157ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

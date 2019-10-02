import unittest
from unittest.mock import patch

from cdf_386A import CodeforcesTask386ASolution


class TestCDF386A(unittest.TestCase):
    def test_386A_acceptance_1(self):
        mock_input = ['2', '5 7']
        expected = '2 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask386ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_386A_acceptance_2(self):
        mock_input = ['3', '10 2 8']
        expected = '1 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask386ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_386A_acceptance_3(self):
        mock_input = ['6', '3 8 2 9 4 14']
        expected = '6 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask386ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

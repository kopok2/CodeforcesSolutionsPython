import unittest
from unittest.mock import patch

from cdf_136A import CodeforcesTask136ASolution


class TestCDF136A(unittest.TestCase):
    def test_136A_acceptance_1(self):
        mock_input = ['4', '2 3 4 1']
        expected = '4 1 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask136ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_136A_acceptance_2(self):
        mock_input = ['3', '1 3 2']
        expected = '1 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask136ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_136A_acceptance_3(self):
        mock_input = ['2', '1 2']
        expected = '1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask136ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

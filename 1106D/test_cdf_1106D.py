import unittest
from unittest.mock import patch

from cdf_1106D import CodeforcesTask1106DSolution


class TestCDF1106D(unittest.TestCase):
    def test_1106D_acceptance_1(self):
        mock_input = ['3 2 1 2 1 3']
        expected = '1 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106DSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106D_acceptance_2(self):
        mock_input = ['5 5 1 4 3 4 5 4 3 2 1 5']
        expected = '1 4 3 2 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106DSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1106D_acceptance_3(self):
        mock_input = ['10 10 1 4 6 8 2 5 3 7 9 4 5 6 3 4 8 10 8 9 1 10']
        expected = '1 4 3 7 9 8 6 5 2 10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1106DSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

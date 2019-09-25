import unittest
from unittest.mock import patch

from cdf_1143C import CodeforcesTask1143CSolution


class TestCDF1143C(unittest.TestCase):
    def test_1143C_acceptance_1(self):
        mock_input = ['5 3 1 1 1 -1 0 2 1 3 0']
        expected = '1 2 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1143CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1143C_acceptance_2(self):
        mock_input = ['5 -1 0 1 1 1 1 2 0 3 0']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1143CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1143C_acceptance_3(self):
        mock_input = ['8 2 1 -1 0 1 0 1 1 1 1 4 0 5 1 7 0']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1143CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

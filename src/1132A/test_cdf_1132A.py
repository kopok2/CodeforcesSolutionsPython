import unittest
from unittest.mock import patch

from cdf_1132A import CodeforcesTask1132ASolution


class TestCDF1132A(unittest.TestCase):
    def test_1132A_acceptance_1(self):
        mock_input = ['3 1 4 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1132ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1132A_acceptance_2(self):
        mock_input = ['0 0 0 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1132ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1132A_acceptance_3(self):
        mock_input = ['1 2 3 4']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1132ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

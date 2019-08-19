import unittest
from unittest.mock import patch

from cdf_1003A import CodeforcesTask1003ASolution


class TestCDF1003A(unittest.TestCase):
    def test_1003A_acceptance_1(self):
        mock_input = ['6', '1 2 4 3 3 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1003ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1003A_acceptance_2(self):
        mock_input = ['1', '100']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1003ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

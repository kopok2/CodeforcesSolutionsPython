import unittest
from unittest.mock import patch

from cdf_415A import CodeforcesTask415ASolution


class TestCDF415A(unittest.TestCase):
    def test_415A_acceptance_1(self):
        mock_input = ['5 4', '4 3 1 2']
        expected = '1 1 3 4 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask415ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_415A_acceptance_2(self):
        mock_input = ['5 5', '5 4 3 2 1']
        expected = '1 2 3 4 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask415ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

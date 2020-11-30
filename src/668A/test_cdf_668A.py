import unittest
from unittest.mock import patch

from cdf_668A import CodeforcesTask668ASolution


class TestCDF668A(unittest.TestCase):
    def test_668A_acceptance_1(self):
        mock_input = ['2 2 6', '2 1', '2 2', '3 1 1 1', '3 2 2 2', '3 1 2 8', '3 2 1 8']
        expected = '8 2\n1 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask668ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_668A_acceptance_2(self):
        mock_input = ['3 3 2', '1 2', '3 2 2 5']
        expected = '0 0 0\n0 0 5\n0 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask668ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

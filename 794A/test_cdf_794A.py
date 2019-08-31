import unittest
from unittest.mock import patch

from cdf_794A import CodeforcesTask794ASolution


class TestCDF794A(unittest.TestCase):
    def test_794A_acceptance_1(self):
        mock_input = ['5 3 7', '8', '4 7 5 5 3 6 2 8']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask794ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_794A_acceptance_2(self):
        mock_input = ['6 5 7', '5', '1 5 7 92 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask794ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

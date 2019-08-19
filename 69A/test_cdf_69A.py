import unittest
from unittest.mock import patch

from cdf_69A import CodeforcesTask69ASolution


class TestCDF69A(unittest.TestCase):
    def test_69A_acceptance_1(self):
        mock_input = ['3', '4 1 7', '-2 4 -1', '1 -5 -3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask69ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_69A_acceptance_2(self):
        mock_input = ['3', '3 -1 7', '-5 2 -4', '2 -1 -3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask69ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

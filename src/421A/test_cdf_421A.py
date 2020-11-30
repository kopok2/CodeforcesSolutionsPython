import unittest
from unittest.mock import patch

from cdf_421A import CodeforcesTask421ASolution


class TestCDF421A(unittest.TestCase):
    def test_421A_acceptance_1(self):
        mock_input = ['4 2 3', '1 2', '2 3 4']
        expected = '1 1 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask421ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_421A_acceptance_2(self):
        mock_input = ['5 5 2', '3 4 1 2 5', '2 3']
        expected = '1 1 1 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask421ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

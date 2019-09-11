import unittest
from unittest.mock import patch

from cdf_888A import CodeforcesTask888ASolution


class TestCDF888A(unittest.TestCase):
    def test_888A_acceptance_1(self):
        mock_input = ['3', '1 2 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask888ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_888A_acceptance_2(self):
        mock_input = ['4', '1 5 2 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask888ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

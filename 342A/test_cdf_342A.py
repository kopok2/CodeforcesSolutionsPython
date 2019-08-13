import unittest
from unittest.mock import patch

from cdf_342A import CodeforcesTask342ASolution


class TestCDF342A(unittest.TestCase):
    def test_342A_acceptance_1(self):
        mock_input = ['6', '1 1 1 2 2 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask342ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_342A_acceptance_2(self):
        mock_input = ['6', '2 2 1 1 4 6']
        expected = '1 2 4\n1 2 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask342ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

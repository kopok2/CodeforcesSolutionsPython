import unittest
from unittest.mock import patch

from cdf_435A import CodeforcesTask435ASolution


class TestCDF435A(unittest.TestCase):
    def test_435A_acceptance_1(self):
        mock_input = ['4 3', '2 3 2 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask435ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_435A_acceptance_2(self):
        mock_input = ['3 4', '1 2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask435ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

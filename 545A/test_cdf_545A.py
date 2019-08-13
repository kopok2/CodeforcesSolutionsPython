import unittest
from unittest.mock import patch

from cdf_545A import CodeforcesTask545ASolution


class TestCDF545A(unittest.TestCase):
    def test_545A_acceptance_1(self):
        mock_input = ['3', '-1 0 0', '0 -1 1', '0 2 -1']
        expected = '2\n1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask545ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_545A_acceptance_2(self):
        mock_input = ['4', '-1 3 3 3', '3 -1 3 3', '3 3 -1 3', '3 3 3 -1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask545ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

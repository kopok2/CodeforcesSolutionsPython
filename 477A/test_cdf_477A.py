import unittest
from unittest.mock import patch

from cdf_477A import CodeforcesTask477ASolution


class TestCDF477A(unittest.TestCase):
    def test_477A_acceptance_1(self):
        mock_input = ['1 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask477ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_477A_acceptance_2(self):
        mock_input = ['2 2']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask477ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

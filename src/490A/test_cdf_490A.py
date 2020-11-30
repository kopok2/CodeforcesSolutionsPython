import unittest
from unittest.mock import patch

from cdf_490A import CodeforcesTask490ASolution


class TestCDF490A(unittest.TestCase):
    def test_490A_acceptance_1(self):
        mock_input = ['7', '1 3 1 3 2 1 2']
        expected = '2\n3 5 2\n6 7 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask490ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_490A_acceptance_2(self):
        mock_input = ['4', '2 1 1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask490ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

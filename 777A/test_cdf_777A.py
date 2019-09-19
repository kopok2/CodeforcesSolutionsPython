import unittest
from unittest.mock import patch

from cdf_777A import CodeforcesTask777ASolution


class TestCDF777A(unittest.TestCase):
    def test_777A_acceptance_1(self):
        mock_input = ['4', '2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask777ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_777A_acceptance_2(self):
        mock_input = ['1', '1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask777ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

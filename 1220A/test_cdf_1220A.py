import unittest
from unittest.mock import patch

from cdf_1220A import CodeforcesTask1220ASolution


class TestCDF1220A(unittest.TestCase):
    def test_1220A_acceptance_1(self):
        mock_input = ['4 ezor']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1220ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1220A_acceptance_2(self):
        mock_input = ['10 nznooeeoer']
        expected = '1 1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1220ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

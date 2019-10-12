import unittest
from unittest.mock import patch

from cdf_1201A import CodeforcesTask1201ASolution


class TestCDF1201A(unittest.TestCase):
    def test_1201A_acceptance_1(self):
        mock_input = ['2 4 ABCD ABCE 1 2 3 4']
        expected = '16'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1201ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1201A_acceptance_2(self):
        mock_input = ['3 3 ABC BCD CDE 5 4 12']
        expected = '21'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1201ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

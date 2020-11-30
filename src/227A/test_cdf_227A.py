import unittest
from unittest.mock import patch

from cdf_227A import CodeforcesTask227ASolution


class TestCDF227A(unittest.TestCase):
    def test_227A_acceptance_1(self):
        mock_input = ['0 0', '0 1', '1 1']
        expected = 'RIGHT'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask227ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_227A_acceptance_2(self):
        mock_input = ['-1 -1', '-3 -3', '-4 -4']
        expected = 'TOWARDS'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask227ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_227A_acceptance_3(self):
        mock_input = ['-4 -6', '-3 -7', '-2 -6']
        expected = 'LEFT'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask227ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

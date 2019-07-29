import unittest
from unittest.mock import patch

from cdf_792A import CodeforcesTask792ASolution


class TestCDF792A(unittest.TestCase):
    def test_792A_acceptance_1(self):
        mock_input = ['4', '6 -3 0 4']
        expected = '2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask792ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_792A_acceptance_2(self):
        mock_input = ['3', '-2 0 2']
        expected = '2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask792ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

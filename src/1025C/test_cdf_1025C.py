import unittest
from unittest.mock import patch

from cdf_1025C import CodeforcesTask1025CSolution


class TestCDF1025C(unittest.TestCase):
    def test_1025C_acceptance_1(self):
        mock_input = ['bwwwbwwbw']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1025CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1025C_acceptance_2(self):
        mock_input = ['bwwbwwb']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1025CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

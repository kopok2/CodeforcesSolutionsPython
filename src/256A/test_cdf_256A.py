import unittest
from unittest.mock import patch

from cdf_256A import CodeforcesTask256ASolution


class TestCDF256A(unittest.TestCase):
    def test_256A_acceptance_1(self):
        mock_input = ['2', '3 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask256ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_256A_acceptance_2(self):
        mock_input = ['4', '10 20 10 30']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask256ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

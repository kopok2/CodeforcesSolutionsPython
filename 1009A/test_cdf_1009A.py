import unittest
from unittest.mock import patch

from cdf_1009A import CodeforcesTask1009ASolution


class TestCDF1009A(unittest.TestCase):
    def test_1009A_acceptance_1(self):
        mock_input = ['5 4', '2 4 5 2 4', '5 3 4 6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1009ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1009A_acceptance_2(self):
        mock_input = ['5 2', '20 40 50 20 40', '19 20']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1009ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1009A_acceptance_3(self):
        mock_input = ['6 4', '4 8 15 16 23 42', '1000 1000 1000 1000']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1009ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

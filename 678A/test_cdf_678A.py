import unittest
from unittest.mock import patch

from cdf_678A import CodeforcesTask678ASolution


class TestCDF678A(unittest.TestCase):
    def test_678A_acceptance_1(self):
        mock_input = ['5 3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask678ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_678A_acceptance_2(self):
        mock_input = ['25 13']
        expected = '26'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask678ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_678A_acceptance_3(self):
        mock_input = ['26 13']
        expected = '39'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask678ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

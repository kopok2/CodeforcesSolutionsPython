import unittest
from unittest.mock import patch

from cdf_68A import CodeforcesTask68ASolution


class TestCDF68A(unittest.TestCase):
    def test_68A_acceptance_1(self):
        mock_input = ['2 7 1 8 2 8']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask68ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_68A_acceptance_2(self):
        mock_input = ['20 30 40 50 0 100']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask68ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_68A_acceptance_3(self):
        mock_input = ['31 41 59 26 17 43']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask68ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

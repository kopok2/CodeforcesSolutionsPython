import unittest
from unittest.mock import patch

from cdf_714A import CodeforcesTask714ASolution


class TestCDF714A(unittest.TestCase):
    def test_714A_acceptance_1(self):
        mock_input = ['1 10 9 20 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask714ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_714A_acceptance_2(self):
        mock_input = ['1 100 50 200 75']
        expected = '50'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask714ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_230A import CodeforcesTask230ASolution


class TestCDF230A(unittest.TestCase):
    def test_230A_acceptance_1(self):
        mock_input = ['2 2', '1 99', '100 0']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask230ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_230A_acceptance_2(self):
        mock_input = ['10 1', '100 100']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask230ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

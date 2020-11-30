import unittest
from unittest.mock import patch

from cdf_31A import CodeforcesTask31ASolution


class TestCDF31A(unittest.TestCase):
    def test_31A_acceptance_1(self):
        mock_input = ['5', '1 2 3 5 7']
        expected = '3 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask31ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_31A_acceptance_2(self):
        mock_input = ['5', '1 8 1 5 1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask31ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

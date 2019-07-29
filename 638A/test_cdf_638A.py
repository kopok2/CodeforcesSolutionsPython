import unittest
from unittest.mock import patch

from cdf_638A import CodeforcesTask638ASolution


class TestCDF638A(unittest.TestCase):
    def test_638A_acceptance_1(self):
        mock_input = ['4 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask638ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_638A_acceptance_2(self):
        mock_input = ['8 5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask638ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

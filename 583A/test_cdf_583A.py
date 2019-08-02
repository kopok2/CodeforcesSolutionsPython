import unittest
from unittest.mock import patch

from cdf_583A import CodeforcesTask583ASolution


class TestCDF583A(unittest.TestCase):
    def test_583A_acceptance_1(self):
        mock_input = ['2', '1 1', '1 2', '2 1', '2 2']
        expected = '1 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask583ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_583A_acceptance_2(self):
        mock_input = ['1', '1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask583ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

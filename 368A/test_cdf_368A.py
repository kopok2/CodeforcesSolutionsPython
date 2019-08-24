import unittest
from unittest.mock import patch

from cdf_368A import CodeforcesTask368ASolution


class TestCDF368A(unittest.TestCase):
    def test_368A_acceptance_1(self):
        mock_input = ['2 1', '2 1', '2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask368ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_368A_acceptance_2(self):
        mock_input = ['2 1', '2 1', '10']
        expected = '-5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask368ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

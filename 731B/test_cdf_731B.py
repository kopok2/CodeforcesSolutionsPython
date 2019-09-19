import unittest
from unittest.mock import patch

from cdf_731B import CodeforcesTask731BSolution


class TestCDF731B(unittest.TestCase):
    def test_731B_acceptance_1(self):
        mock_input = ['4', '1 2 1 2']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask731BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_731B_acceptance_2(self):
        mock_input = ['3', '1 0 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask731BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

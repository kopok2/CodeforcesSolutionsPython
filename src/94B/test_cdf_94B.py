import unittest
from unittest.mock import patch

from cdf_94B import CodeforcesTask94BSolution


class TestCDF94B(unittest.TestCase):
    def test_94B_acceptance_1(self):
        mock_input = ['4', '1 3', '2 3', '1 4', '5 3']
        expected = 'WIN'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask94BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_94B_acceptance_2(self):
        mock_input = ['5', '1 2', '2 3', '3 4', '4 5', '5 1']
        expected = 'FAIL'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask94BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

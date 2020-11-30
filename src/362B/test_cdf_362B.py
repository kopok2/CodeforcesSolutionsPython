import unittest
from unittest.mock import patch

from cdf_362B import CodeforcesTask362BSolution


class TestCDF362B(unittest.TestCase):
    def test_362B_acceptance_1(self):
        mock_input = ['10 5', '2 4 8 3 6']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask362BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_362B_acceptance_2(self):
        mock_input = ['10 5', '2 4 5 7 9']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask362BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

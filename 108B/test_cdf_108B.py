import unittest
from unittest.mock import patch

from cdf_108B import CodeforcesTask108BSolution


class TestCDF108B(unittest.TestCase):
    def test_108B_acceptance_1(self):
        mock_input = ['3', '64 16 32']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask108BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_108B_acceptance_2(self):
        mock_input = ['4', '4 2 1 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask108BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

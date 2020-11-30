import unittest
from unittest.mock import patch

from cdf_890B import CodeforcesTask890BSolution


class TestCDF890B(unittest.TestCase):
    def test_890B_acceptance_1(self):
        mock_input = ['5', '1 3 2 1 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask890BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_890B_acceptance_2(self):
        mock_input = ['6', '2 1 2 2 4 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask890BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

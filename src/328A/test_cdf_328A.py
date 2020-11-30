import unittest
from unittest.mock import patch

from cdf_328A import CodeforcesTask328ASolution


class TestCDF328A(unittest.TestCase):
    def test_328A_acceptance_1(self):
        mock_input = ['836 624 412 200']
        expected = '-12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask328ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_328A_acceptance_2(self):
        mock_input = ['1 334 667 1000']
        expected = '1333'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask328ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_863B import CodeforcesTask863BSolution


class TestCDF863B(unittest.TestCase):
    def test_863B_acceptance_1(self):
        mock_input = ['2', '1 2 3 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask863BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_863B_acceptance_2(self):
        mock_input = ['4', '1 3 4 6 3 4 100 200']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask863BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

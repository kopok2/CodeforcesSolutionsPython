import unittest
from unittest.mock import patch

from cdf_408B import CodeforcesTask408BSolution


class TestCDF408B(unittest.TestCase):
    def test_408B_acceptance_1(self):
        mock_input = ['aaabbac', 'aabbccac']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask408BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_408B_acceptance_2(self):
        mock_input = ['a', 'z']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask408BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

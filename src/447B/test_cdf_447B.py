import unittest
from unittest.mock import patch

from cdf_447B import CodeforcesTask447BSolution


class TestCDF447B(unittest.TestCase):
    def test_447B_acceptance_1(self):
        mock_input = ['abc', '3', '1 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1']
        expected = '41'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask447BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

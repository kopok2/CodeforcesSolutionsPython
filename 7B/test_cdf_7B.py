import unittest
from unittest.mock import patch

from cdf_7B import CodeforcesTask7BSolution


class TestCDF7B(unittest.TestCase):
    def test_7B_acceptance_1(self):
        mock_input = ['6 10', 'alloc 5', 'alloc 3', 'erase 1', 'alloc 6', 'defragment', 'alloc 6']
        expected = '1\n2\nNULL\n3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask7BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

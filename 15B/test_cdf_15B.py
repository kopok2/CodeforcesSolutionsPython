import unittest
from unittest.mock import patch

from cdf_15B import CodeforcesTask15BSolution


class TestCDF15B(unittest.TestCase):
    def test_15B_acceptance_1(self):
        mock_input = ['2', '4 4 1 1 3 3', '4 3 1 1 2 2']
        expected = '8\n2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask15BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

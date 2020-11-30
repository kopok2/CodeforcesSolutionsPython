import unittest
from unittest.mock import patch

from cdf_239B import CodeforcesTask239BSolution


class TestCDF239B(unittest.TestCase):
    def test_239B_acceptance_1(self):
        mock_input = ['7 4', '1>3>22<', '1 3', '4 7', '7 7', '1 7']
        expected = '0 1 0 1 0 0 0 0 0 0\n2 2 2 0 0 0 0 0 0 0\n0 0 0 0 0 0 0 0 0 0\n2 3 2 1 0 0 0 0 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask239BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

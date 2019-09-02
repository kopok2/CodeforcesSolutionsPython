import unittest
from unittest.mock import patch

from cdf_317B import CodeforcesTask317BSolution


class TestCDF317B(unittest.TestCase):
    def test_317B_acceptance_1(self):
        mock_input = ['1 3', '0 1', '0 0', '0 -1']
        expected = '0\n1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask317BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_317B_acceptance_2(self):
        mock_input = ['6 5', '0 -2', '0 -1', '0 0', '0 1', '0 2']
        expected = '0\n1\n2\n1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask317BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

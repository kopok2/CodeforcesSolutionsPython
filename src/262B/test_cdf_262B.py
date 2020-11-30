import unittest
from unittest.mock import patch

from cdf_262B import CodeforcesTask262BSolution


class TestCDF262B(unittest.TestCase):
    def test_262B_acceptance_1(self):
        mock_input = ['3 2', '-1 -1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask262BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_262B_acceptance_2(self):
        mock_input = ['3 1', '-1 -1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask262BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

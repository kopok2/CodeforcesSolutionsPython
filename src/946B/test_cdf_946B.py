import unittest
from unittest.mock import patch

from cdf_946B import CodeforcesTask946BSolution


class TestCDF946B(unittest.TestCase):
    def test_946B_acceptance_1(self):
        mock_input = ['12 5']
        expected = '0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask946BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_946B_acceptance_2(self):
        mock_input = ['31 12']
        expected = '7 12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask946BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

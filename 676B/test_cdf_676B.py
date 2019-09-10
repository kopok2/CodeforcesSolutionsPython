import unittest
from unittest.mock import patch

from cdf_676B import CodeforcesTask676BSolution


class TestCDF676B(unittest.TestCase):
    def test_676B_acceptance_1(self):
        mock_input = ['3 5']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask676BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_676B_acceptance_2(self):
        mock_input = ['4 8']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask676BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

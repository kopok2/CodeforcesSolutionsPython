import unittest
from unittest.mock import patch

from cdf_110B import CodeforcesTask110BSolution


class TestCDF110B(unittest.TestCase):
    def test_110B_acceptance_1(self):
        mock_input = ['5']
        expected = 'abcda'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask110BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_110B_acceptance_2(self):
        mock_input = ['3']
        expected = 'abc'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask110BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

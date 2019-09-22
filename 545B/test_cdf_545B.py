import unittest
from unittest.mock import patch

from cdf_545B import CodeforcesTask545BSolution


class TestCDF545B(unittest.TestCase):
    def test_545B_acceptance_1(self):
        mock_input = ['0001', '1011']
        expected = '0011'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask545BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_545B_acceptance_2(self):
        mock_input = ['000', '111']
        expected = 'impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask545BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

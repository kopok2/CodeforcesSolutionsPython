import unittest
from unittest.mock import patch

from cdf_90B import CodeforcesTask90BSolution


class TestCDF90B(unittest.TestCase):
    def test_90B_acceptance_1(self):
        mock_input = ['3 3', 'cba', 'bcd', 'cbc']
        expected = 'abcd'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask90BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_90B_acceptance_2(self):
        mock_input = ['5 5', 'fcofd', 'ooedo', 'afaoa', 'rdcdf', 'eofsf']
        expected = 'codeforces'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask90BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

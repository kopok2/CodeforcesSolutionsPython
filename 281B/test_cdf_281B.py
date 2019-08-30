import unittest
from unittest.mock import patch

from cdf_281B import CodeforcesTask281BSolution


class TestCDF281B(unittest.TestCase):
    def test_281B_acceptance_1(self):
        mock_input = ['3 7 6']
        expected = '2/5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask281BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_281B_acceptance_2(self):
        mock_input = ['7 2 4']
        expected = '7/2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask281BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

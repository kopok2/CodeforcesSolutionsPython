import unittest
from unittest.mock import patch

from cdf_221B import CodeforcesTask221BSolution


class TestCDF221B(unittest.TestCase):
    def test_221B_acceptance_1(self):
        mock_input = ['1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask221BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_221B_acceptance_2(self):
        mock_input = ['10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask221BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

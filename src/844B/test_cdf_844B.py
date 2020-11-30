import unittest
from unittest.mock import patch

from cdf_844B import CodeforcesTask844BSolution


class TestCDF844B(unittest.TestCase):
    def test_844B_acceptance_1(self):
        mock_input = ['1 1', '0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask844BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_844B_acceptance_2(self):
        mock_input = ['2 3', '1 0 1', '0 1 0']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask844BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

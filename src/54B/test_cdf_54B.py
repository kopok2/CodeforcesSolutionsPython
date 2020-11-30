import unittest
from unittest.mock import patch

from cdf_54B import CodeforcesTask54BSolution


class TestCDF54B(unittest.TestCase):
    def test_54B_acceptance_1(self):
        mock_input = ['2 4', 'ABDC', 'ABDC']
        expected = '3\n2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask54BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_54B_acceptance_2(self):
        mock_input = ['2 6', 'ABCCBA', 'ABCCBA']
        expected = '1\n2 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask54BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

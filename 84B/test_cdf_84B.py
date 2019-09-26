import unittest
from unittest.mock import patch

from cdf_84B import CodeforcesTask84BSolution


class TestCDF84B(unittest.TestCase):
    def test_84B_acceptance_1(self):
        mock_input = ['4', '2 1 1 4']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask84BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_84B_acceptance_2(self):
        mock_input = ['5', '-2 -2 -2 0 1']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask84BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

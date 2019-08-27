import unittest
from unittest.mock import patch

from cdf_265B import CodeforcesTask265BSolution


class TestCDF265B(unittest.TestCase):
    def test_265B_acceptance_1(self):
        mock_input = ['2', '1', '2']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask265BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_265B_acceptance_2(self):
        mock_input = ['5', '2', '1', '2', '1', '1']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask265BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

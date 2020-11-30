import unittest
from unittest.mock import patch

from cdf_719B import CodeforcesTask719BSolution


class TestCDF719B(unittest.TestCase):
    def test_719B_acceptance_1(self):
        mock_input = ['5', 'rbbrr']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_719B_acceptance_2(self):
        mock_input = ['5', 'bbbbb']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_719B_acceptance_3(self):
        mock_input = ['3', 'rbr']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask719BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

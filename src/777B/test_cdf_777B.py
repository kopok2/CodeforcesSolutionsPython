import unittest
from unittest.mock import patch

from cdf_777B import CodeforcesTask777BSolution


class TestCDF777B(unittest.TestCase):
    def test_777B_acceptance_1(self):
        mock_input = ['3', '123', '321']
        expected = '0\n2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask777BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_777B_acceptance_2(self):
        mock_input = ['2', '88', '00']
        expected = '2\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask777BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

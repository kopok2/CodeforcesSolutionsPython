import unittest
from unittest.mock import patch

from cdf_962B import CodeforcesTask962BSolution


class TestCDF962B(unittest.TestCase):
    def test_962B_acceptance_1(self):
        mock_input = ['5 1 1', '*...*']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_962B_acceptance_2(self):
        mock_input = ['6 2 3', '*...*.']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_962B_acceptance_3(self):
        mock_input = ['11 3 10', '.*....**.*.']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_962B_acceptance_4(self):
        mock_input = ['3 2 3', '***']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

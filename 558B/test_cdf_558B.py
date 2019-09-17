import unittest
from unittest.mock import patch

from cdf_558B import CodeforcesTask558BSolution


class TestCDF558B(unittest.TestCase):
    def test_558B_acceptance_1(self):
        mock_input = ['5', '1 1 2 2 1']
        expected = '1 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_558B_acceptance_2(self):
        mock_input = ['5', '1 2 2 3 1']
        expected = '2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_558B_acceptance_3(self):
        mock_input = ['6', '1 2 2 1 1 2']
        expected = '1 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask558BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

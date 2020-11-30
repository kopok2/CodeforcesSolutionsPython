import unittest
from unittest.mock import patch

from cdf_224B import CodeforcesTask224BSolution


class TestCDF224B(unittest.TestCase):
    def test_224B_acceptance_1(self):
        mock_input = ['4 2', '1 2 2 3']
        expected = '1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask224BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_224B_acceptance_2(self):
        mock_input = ['8 3', '1 1 2 2 3 3 4 5']
        expected = '2 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask224BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_224B_acceptance_3(self):
        mock_input = ['7 4', '4 7 7 4 7 4 7']
        expected = '-1 -1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask224BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

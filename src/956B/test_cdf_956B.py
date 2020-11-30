import unittest
from unittest.mock import patch

from cdf_956B import CodeforcesTask956BSolution


class TestCDF956B(unittest.TestCase):
    def test_956B_acceptance_1(self):
        mock_input = ['4 4', '1 3 5 7']
        expected = '0.5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask956BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_956B_acceptance_2(self):
        mock_input = ['10 8', '10 13 15 16 17 19 20 22 24 25']
        expected = '0.875'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask956BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_956B_acceptance_3(self):
        mock_input = ['3 1', '2 5 10']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask956BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_893C import CodeforcesTask893CSolution


class TestCDF893C(unittest.TestCase):
    def test_893C_acceptance_1(self):
        mock_input = ['5 2', '2 5 3 4 8', '1 4', '4 5']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask893CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_893C_acceptance_2(self):
        mock_input = ['10 0', '1 2 3 4 5 6 7 8 9 10']
        expected = '55'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask893CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_893C_acceptance_3(self):
        mock_input = ['10 5', '1 6 2 7 3 8 4 9 5 10', '1 2', '3 4', '5 6', '7 8', '9 10']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask893CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

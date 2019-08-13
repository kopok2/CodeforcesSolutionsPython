import unittest
from unittest.mock import patch

from cdf_915B import CodeforcesTask915BSolution


class TestCDF915B(unittest.TestCase):
    def test_915B_acceptance_1(self):
        mock_input = ['6 3 2 4']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask915BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_915B_acceptance_2(self):
        mock_input = ['6 3 1 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask915BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_915B_acceptance_3(self):
        mock_input = ['5 2 1 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask915BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

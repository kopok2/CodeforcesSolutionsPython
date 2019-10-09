import unittest
from unittest.mock import patch

from cdf_129B import CodeforcesTask129BSolution


class TestCDF129B(unittest.TestCase):
    def test_129B_acceptance_1(self):
        mock_input = ['3 3', '1 2', '2 3', '3 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_129B_acceptance_2(self):
        mock_input = ['6 3', '1 2', '2 3', '3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_129B_acceptance_3(self):
        mock_input = ['6 5', '1 4', '2 4', '3 4', '5 4', '6 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

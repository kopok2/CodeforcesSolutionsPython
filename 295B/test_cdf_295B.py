import unittest
from unittest.mock import patch

from cdf_295B import CodeforcesTask295BSolution


class TestCDF295B(unittest.TestCase):
    def test_295B_acceptance_1(self):
        mock_input = ['1', '0', '1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask295BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_295B_acceptance_2(self):
        mock_input = ['2', '0 5', '4 0', '1 2']
        expected = '9 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask295BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_295B_acceptance_3(self):
        mock_input = ['4', '0 3 1 1', '6 0 400 1', '2 4 0 1', '1 1 1 0', '4 1 2 3']
        expected = '17 23 404 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask295BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

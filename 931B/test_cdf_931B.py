import unittest
from unittest.mock import patch

from cdf_931B import CodeforcesTask931BSolution


class TestCDF931B(unittest.TestCase):
    def test_931B_acceptance_1(self):
        mock_input = ['4 1 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_931B_acceptance_2(self):
        mock_input = ['8 2 6']
        expected = 'Final!'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_931B_acceptance_3(self):
        mock_input = ['8 7 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

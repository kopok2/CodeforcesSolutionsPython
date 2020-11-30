import unittest
from unittest.mock import patch

from cdf_1138B import CodeforcesTask1138BSolution


class TestCDF1138B(unittest.TestCase):
    def test_1138B_acceptance_1(self):
        mock_input = ['4 0011 0101']
        expected = '1 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1138BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1138B_acceptance_2(self):
        mock_input = ['6 000000 111111']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1138BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1138B_acceptance_3(self):
        mock_input = ['4 0011 1100']
        expected = '4 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1138BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1138B_acceptance_4(self):
        mock_input = ['8 00100101 01111100']
        expected = '1 2 3 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1138BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

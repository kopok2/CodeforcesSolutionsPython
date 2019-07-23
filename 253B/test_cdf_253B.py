import unittest
from unittest.mock import patch

from cdf_253B import CodeforcesTask253BSolution


class TestCDF253B(unittest.TestCase):
    def test_253B_acceptance_1(self):
        mock_input = ['6', '4 5 3 8 3 7']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask253BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_253B_acceptance_2(self):
        mock_input = ['4', '4 3 2 4']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask253BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

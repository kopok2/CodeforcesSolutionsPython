import unittest
from unittest.mock import patch

from cdf_861A import CodeforcesTask861ASolution


class TestCDF861A(unittest.TestCase):
    def test_861A_acceptance_1(self):
        mock_input = ['375 4']
        expected = '30000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask861ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_861A_acceptance_2(self):
        mock_input = ['10000 1']
        expected = '10000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask861ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_861A_acceptance_3(self):
        mock_input = ['38101 0']
        expected = '38101'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask861ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_861A_acceptance_4(self):
        mock_input = ['123456789 8']
        expected = '12345678900000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask861ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

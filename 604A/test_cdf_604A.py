import unittest
from unittest.mock import patch

from cdf_604A import CodeforcesTask604ASolution


class TestCDF604A(unittest.TestCase):
    def test_604A_acceptance_1(self):
        mock_input = ['20 40 60 80 100', '0 1 2 3 4', '1 0']
        expected = '4900'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask604ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_604A_acceptance_2(self):
        mock_input = ['119 119 119 119 119', '0 0 0 0 0', '10 0']
        expected = '4930'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask604ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

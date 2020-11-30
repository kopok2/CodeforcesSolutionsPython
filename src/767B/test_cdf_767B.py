import unittest
from unittest.mock import patch

from cdf_767B import CodeforcesTask767BSolution


class TestCDF767B(unittest.TestCase):
    def test_767B_acceptance_1(self):
        mock_input = ['10 15 2', '2', '10 13']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask767BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_767B_acceptance_2(self):
        mock_input = ['8 17 3', '4', '3 4 5 8']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask767BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

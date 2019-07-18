import unittest
from unittest.mock import patch

from cdf_289A import CodeforcesTask289ASolution


class TestCDF289A(unittest.TestCase):
    def test_289A_acceptance_1(self):
        mock_input = ['2 3', '1 2', '3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask289ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_289A_acceptance_2(self):
        mock_input = ['3 7', '1 2', '3 3', '4 7']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask289ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

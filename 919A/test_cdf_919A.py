import unittest
from unittest.mock import patch

from cdf_919A import CodeforcesTask919ASolution


class TestCDF919A(unittest.TestCase):
    def test_919A_acceptance_1(self):
        mock_input = ['3 5', '1 2', '3 4', '1 3']
        expected = '1.66666667'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask919ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_919A_acceptance_2(self):
        mock_input = ['2 1', '99 100', '98 99']
        expected = '0.98989899'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask919ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

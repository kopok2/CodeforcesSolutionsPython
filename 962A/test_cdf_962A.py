import unittest
from unittest.mock import patch

from cdf_962A import CodeforcesTask962ASolution


class TestCDF962A(unittest.TestCase):
    def test_962A_acceptance_1(self):
        mock_input = ['4', '1 3 2 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_962A_acceptance_2(self):
        mock_input = ['6', '2 2 2 2 2 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask962ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

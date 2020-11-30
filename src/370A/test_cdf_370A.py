import unittest
from unittest.mock import patch

from cdf_370A import CodeforcesTask370ASolution


class TestCDF370A(unittest.TestCase):
    def test_370A_acceptance_1(self):
        mock_input = ['4 3 1 6']
        expected = '2 1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask370ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_370A_acceptance_2(self):
        mock_input = ['5 5 5 6']
        expected = '1 0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask370ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

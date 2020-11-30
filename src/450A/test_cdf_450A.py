import unittest
from unittest.mock import patch

from cdf_450A import CodeforcesTask450ASolution


class TestCDF450A(unittest.TestCase):
    def test_450A_acceptance_1(self):
        mock_input = ['5 2', '1 3 1 4 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask450ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_450A_acceptance_2(self):
        mock_input = ['6 4', '1 1 2 2 3 3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask450ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

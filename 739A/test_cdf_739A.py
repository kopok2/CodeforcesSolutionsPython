import unittest
from unittest.mock import patch

from cdf_739A import CodeforcesTask739ASolution


class TestCDF739A(unittest.TestCase):
    def test_739A_acceptance_1(self):
        mock_input = ['5 3', '1 3', '2 5', '4 5']
        expected = '2\n1 0 2 1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask739ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_739A_acceptance_2(self):
        mock_input = ['4 2', '1 4', '2 4']
        expected = '3\n5 2 0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask739ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

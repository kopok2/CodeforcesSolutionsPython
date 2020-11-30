import unittest
from unittest.mock import patch

from cdf_901A import CodeforcesTask901ASolution


class TestCDF901A(unittest.TestCase):
    def test_901A_acceptance_1(self):
        mock_input = ['2', '1 1 1']
        expected = 'perfect'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask901ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_901A_acceptance_2(self):
        mock_input = ['2', '1 2 2']
        expected = 'ambiguous\n0 1 1 3 3\n0 1 1 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask901ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

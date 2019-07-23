import unittest
from unittest.mock import patch

from cdf_22A import CodeforcesTask22ASolution


class TestCDF22A(unittest.TestCase):
    def test_22A_acceptance_1(self):
        mock_input = ['4', '1 2 2 -4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask22ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_22A_acceptance_2(self):
        mock_input = ['5', '1 2 3 1 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask22ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

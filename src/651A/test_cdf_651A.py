import unittest
from unittest.mock import patch

from cdf_651A import CodeforcesTask651ASolution


class TestCDF651A(unittest.TestCase):
    def test_651A_acceptance_1(self):
        mock_input = ['3 5']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask651ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_651A_acceptance_2(self):
        mock_input = ['4 4']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask651ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

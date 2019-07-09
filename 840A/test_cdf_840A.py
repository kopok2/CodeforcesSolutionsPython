import unittest
from unittest.mock import patch

from cdf_840A import CodeforcesTask840ASolution


class TestCDF840A(unittest.TestCase):
    def test_840A_acceptance_1(self):
        mock_input = ['5', '7 3 5 3 4', '2 1 3 2 3']
        expected = '4 7 3 5 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask840ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_840A_acceptance_2(self):
        mock_input = ['7', '4 6 5 8 8 2 6', '2 1 2 2 1 1 2']
        expected = '2 6 4 5 8 8 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask840ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_978A import CodeforcesTask978ASolution


class TestCDF978A(unittest.TestCase):
    def test_978A_acceptance_1(self):
        mock_input = ['6', '1 5 5 1 6 1']
        expected = '3\n5 6 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask978ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_978A_acceptance_2(self):
        mock_input = ['5', '2 4 2 4 4']
        expected = '2\n2 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask978ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_978A_acceptance_3(self):
        mock_input = ['5', '6 6 6 6 6']
        expected = '1\n6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask978ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

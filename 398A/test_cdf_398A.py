import unittest
from unittest.mock import patch

from cdf_398A import CodeforcesTask398ASolution


class TestCDF398A(unittest.TestCase):
    def test_398A_acceptance_1(self):
        mock_input = ['2 3']
        expected = '-1\nxoxox'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask398ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_398A_acceptance_2(self):
        mock_input = ['4 0']
        expected = '16\noooo'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask398ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_398A_acceptance_3(self):
        mock_input = ['0 4']
        expected = '-16\nxxxx'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask398ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

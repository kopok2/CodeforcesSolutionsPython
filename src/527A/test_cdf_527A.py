import unittest
from unittest.mock import patch

from cdf_527A import CodeforcesTask527ASolution


class TestCDF527A(unittest.TestCase):
    def test_527A_acceptance_1(self):
        mock_input = ['2 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask527ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_527A_acceptance_2(self):
        mock_input = ['10 7']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask527ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_527A_acceptance_3(self):
        mock_input = ['1000000000000 1']
        expected = '1000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask527ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

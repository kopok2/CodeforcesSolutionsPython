import unittest
from unittest.mock import patch

from cdf_999A import CodeforcesTask999ASolution


class TestCDF999A(unittest.TestCase):
    def test_999A_acceptance_1(self):
        mock_input = ['8 4', '4 2 3 1 5 1 6 4']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_999A_acceptance_2(self):
        mock_input = ['5 2', '3 1 2 1 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_999A_acceptance_3(self):
        mock_input = ['5 100', '12 34 55 43 21']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

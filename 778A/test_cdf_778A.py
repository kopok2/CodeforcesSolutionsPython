import unittest
from unittest.mock import patch

from cdf_778A import CodeforcesTask778ASolution


class TestCDF778A(unittest.TestCase):
    def test_778A_acceptance_1(self):
        mock_input = ['ababcba', 'abb', '5 3 4 1 7 6 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask778ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_778A_acceptance_2(self):
        mock_input = ['bbbabb', 'bb', '1 6 3 4 2 5']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask778ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

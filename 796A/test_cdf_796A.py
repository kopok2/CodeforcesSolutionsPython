import unittest
from unittest.mock import patch

from cdf_796A import CodeforcesTask796ASolution


class TestCDF796A(unittest.TestCase):
    def test_796A_acceptance_1(self):
        mock_input = ['5 1 20', '0 27 32 21 19']
        expected = '40'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask796ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_796A_acceptance_2(self):
        mock_input = ['7 3 50', '62 0 0 0 99 33 22']
        expected = '30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask796ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_796A_acceptance_3(self):
        mock_input = ['10 5 100', '1 0 1 0 0 0 0 0 1 1']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask796ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

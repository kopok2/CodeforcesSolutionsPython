import unittest
from unittest.mock import patch

from cdf_768A import CodeforcesTask768ASolution


class TestCDF768A(unittest.TestCase):
    def test_768A_acceptance_1(self):
        mock_input = ['2', '1 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask768ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_768A_acceptance_2(self):
        mock_input = ['3', '1 2 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask768ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

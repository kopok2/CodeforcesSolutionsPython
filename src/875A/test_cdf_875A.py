import unittest
from unittest.mock import patch

from cdf_875A import CodeforcesTask875ASolution


class TestCDF875A(unittest.TestCase):
    def test_875A_acceptance_1(self):
        mock_input = ['21']
        expected = '1\n15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask875ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_875A_acceptance_2(self):
        mock_input = ['20']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask875ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

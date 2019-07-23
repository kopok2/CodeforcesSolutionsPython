import unittest
from unittest.mock import patch

from cdf_332A import CodeforcesTask332ASolution


class TestCDF332A(unittest.TestCase):
    def test_332A_acceptance_1(self):
        mock_input = ['4', 'abbba']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask332ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_332A_acceptance_2(self):
        mock_input = ['4', 'abbab']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask332ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

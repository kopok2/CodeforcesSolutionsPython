import unittest
from unittest.mock import patch

from cdf_1139A import CodeforcesTask1139ASolution


class TestCDF1139A(unittest.TestCase):
    def test_1139A_acceptance_1(self):
        mock_input = ['4 1234']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1139ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1139A_acceptance_2(self):
        mock_input = ['4 2244']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1139ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

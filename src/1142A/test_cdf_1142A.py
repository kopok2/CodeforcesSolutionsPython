import unittest
from unittest.mock import patch

from cdf_1142A import CodeforcesTask1142ASolution


class TestCDF1142A(unittest.TestCase):
    def test_1142A_acceptance_1(self):
        mock_input = ['2 3 1 1']
        expected = '1 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1142ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1142A_acceptance_2(self):
        mock_input = ['3 2 0 0']
        expected = '1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1142ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1142A_acceptance_3(self):
        mock_input = ['1 10 5 3']
        expected = '5 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1142ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

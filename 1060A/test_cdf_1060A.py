import unittest
from unittest.mock import patch

from cdf_1060A import CodeforcesTask1060ASolution


class TestCDF1060A(unittest.TestCase):
    def test_1060A_acceptance_1(self):
        mock_input = ['11', '00000000008']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1060ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1060A_acceptance_2(self):
        mock_input = ['22', '0011223344556677889988']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1060ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1060A_acceptance_3(self):
        mock_input = ['11', '31415926535']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1060ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

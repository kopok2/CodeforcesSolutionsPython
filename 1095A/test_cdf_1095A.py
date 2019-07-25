import unittest
from unittest.mock import patch

from cdf_1095A import CodeforcesTask1095ASolution


class TestCDF1095A(unittest.TestCase):
    def test_1095A_acceptance_1(self):
        mock_input = ['6 baabbb']
        expected = 'bab'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1095ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1095A_acceptance_2(self):
        mock_input = ['10 ooopppssss']
        expected = 'oops'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1095ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1095A_acceptance_3(self):
        mock_input = ['1 z']
        expected = 'z'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1095ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

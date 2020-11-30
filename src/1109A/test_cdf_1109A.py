import unittest
from unittest.mock import patch

from cdf_1109A import CodeforcesTask1109ASolution


class TestCDF1109A(unittest.TestCase):
    def test_1109A_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1109ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1109A_acceptance_2(self):
        mock_input = ['6', '3 2 2 3 7 6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1109ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1109A_acceptance_3(self):
        mock_input = ['3', '42 4 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1109ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

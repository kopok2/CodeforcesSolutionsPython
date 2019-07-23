import unittest
from unittest.mock import patch

from cdf_414A import CodeforcesTask414ASolution


class TestCDF414A(unittest.TestCase):
    def test_414A_acceptance_1(self):
        mock_input = ['5 2']
        expected = '1 2 3 4 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask414ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_414A_acceptance_2(self):
        mock_input = ['5 3']
        expected = '2 4 3 7 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask414ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_414A_acceptance_3(self):
        mock_input = ['7 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask414ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

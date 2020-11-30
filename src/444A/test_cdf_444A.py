import unittest
from unittest.mock import patch

from cdf_444A import CodeforcesTask444ASolution


class TestCDF444A(unittest.TestCase):
    def test_444A_acceptance_1(self):
        mock_input = ['1 0', '1']
        expected = '0.000000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask444ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_444A_acceptance_2(self):
        mock_input = ['2 1', '1 2', '1 2 1']
        expected = '3.000000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask444ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_444A_acceptance_3(self):
        mock_input = ['5 6', '13 56 73 98 17', '1 2 56', '1 3 29', '1 4 42', '2 3 95', '2 4 88', '3 4 63']
        expected = '2.965517241379311'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask444ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

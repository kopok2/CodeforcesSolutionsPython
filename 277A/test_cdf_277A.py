import unittest
from unittest.mock import patch

from cdf_277A import CodeforcesTask277ASolution


class TestCDF277A(unittest.TestCase):
    def test_277A_acceptance_1(self):
        mock_input = ['5 5', '1 2', '2 2 3', '2 3 4', '2 4 5', '1 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask277ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_277A_acceptance_2(self):
        mock_input = ['8 7', '0', '3 1 2 3', '1 1', '2 5 4', '2 6 7', '1 3', '2 7 4', '1 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask277ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_277A_acceptance_3(self):
        mock_input = ['2 2', '1 2', '0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask277ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

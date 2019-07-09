import unittest
from unittest.mock import patch

from cdf_57A import CodeforcesTask57ASolution


class TestCDF57A(unittest.TestCase):
    def test_57A_acceptance_1(self):
        mock_input = ['2 0 0 1 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask57ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_57A_acceptance_2(self):
        mock_input = ['2 0 1 2 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask57ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_57A_acceptance_3(self):
        mock_input = ['100 0 0 100 100']
        expected = '200'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask57ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

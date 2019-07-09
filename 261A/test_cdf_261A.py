import unittest
from unittest.mock import patch

from cdf_261A import CodeforcesTask261ASolution


class TestCDF261A(unittest.TestCase):
    def test_261A_acceptance_1(self):
        mock_input = ['1', '2', '4', '50 50 100 100']
        expected = '200'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask261ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_261A_acceptance_2(self):
        mock_input = ['2', '2 3', '5', '50 50 50 50 50']
        expected = '150'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask261ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_261A_acceptance_3(self):
        mock_input = ['1', '1', '7', '1 1 1 1 1 1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask261ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_263A import CodeforcesTask263ASolution


class TestCDF263A(unittest.TestCase):
    def test_263A_acceptance_1(self):
        mock_input = ['0 0 0 0 0', '0 0 0 0 1', '0 0 0 0 0', '0 0 0 0 0', '0 0 0 0 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask263ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_263A_acceptance_2(self):
        mock_input = ['0 0 0 0 0', '0 0 0 0 0', '0 1 0 0 0', '0 0 0 0 0', '0 0 0 0 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask263ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

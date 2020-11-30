import unittest
from unittest.mock import patch

from cdf_1143A import CodeforcesTask1143ASolution


class TestCDF1143A(unittest.TestCase):
    def test_1143A_acceptance_1(self):
        mock_input = ['5 0 0 1 0 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1143ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_1143A_acceptance_2(self):
        mock_input = ['4 1 0 0 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1143ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_610A import CodeforcesTask610ASolution


class TestCDF610A(unittest.TestCase):
    def test_610A_acceptance_1(self):
        mock_input = ['6']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask610ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_610A_acceptance_2(self):
        mock_input = ['20']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask610ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

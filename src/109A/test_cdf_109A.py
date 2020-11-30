import unittest
from unittest.mock import patch

from cdf_109A import CodeforcesTask109ASolution


class TestCDF109A(unittest.TestCase):
    def test_109A_acceptance_1(self):
        mock_input = ['11']
        expected = '47'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask109ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_109A_acceptance_2(self):
        mock_input = ['10']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask109ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

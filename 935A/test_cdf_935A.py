import unittest
from unittest.mock import patch

from cdf_935A import CodeforcesTask935ASolution


class TestCDF935A(unittest.TestCase):
    def test_935A_acceptance_1(self):
        mock_input = ['2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask935ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_935A_acceptance_2(self):
        mock_input = ['10']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask935ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

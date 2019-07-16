import unittest
from unittest.mock import patch

from cdf_686A import CodeforcesTask686ASolution


class TestCDF686A(unittest.TestCase):
    def test_686A_acceptance_1(self):
        mock_input = ['5 7', '+ 5', '- 10', '- 20', '+ 40', '- 20']
        expected = '22 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask686ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_686A_acceptance_2(self):
        mock_input = ['5 17', '- 16', '- 2', '- 98', '+ 100', '- 98']
        expected = '3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask686ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

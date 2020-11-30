import unittest
from unittest.mock import patch

from cdf_607A import CodeforcesTask607ASolution


class TestCDF607A(unittest.TestCase):
    def test_607A_acceptance_1(self):
        mock_input = ['4', '1 9', '3 1', '6 1', '7 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask607ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_607A_acceptance_2(self):
        mock_input = ['7', '1 1', '2 1', '3 1', '4 1', '5 1', '6 1', '7 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask607ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

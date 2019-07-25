import unittest
from unittest.mock import patch

from cdf_33A import CodeforcesTask33ASolution


class TestCDF33A(unittest.TestCase):
    def test_33A_acceptance_1(self):
        mock_input = ['4 3 18', '2 3', '1 2', '3 6', '2 3']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask33ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_33A_acceptance_2(self):
        mock_input = ['2 2 13', '1 13', '2 12']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask33ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

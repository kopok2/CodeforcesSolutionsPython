import unittest
from unittest.mock import patch

from cdf_241A import CodeforcesTask241ASolution


class TestCDF241A(unittest.TestCase):
    def test_241A_acceptance_1(self):
        mock_input = ['4 6', '1 2 5 2', '2 3 3 4']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask241ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_241A_acceptance_2(self):
        mock_input = ['2 3', '5 6', '5 5']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask241ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

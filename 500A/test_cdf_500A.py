import unittest
from unittest.mock import patch

from cdf_500A import CodeforcesTask500ASolution


class TestCDF500A(unittest.TestCase):
    def test_500A_acceptance_1(self):
        mock_input = ['8 4', '1 2 1 2 1 2 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask500ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_500A_acceptance_2(self):
        mock_input = ['8 5', '1 2 1 2 1 1 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask500ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

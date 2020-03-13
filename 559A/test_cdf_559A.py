import unittest
from unittest.mock import patch

from cdf_559A import CodeforcesTask559ASolution


class TestCDF559A(unittest.TestCase):
    def test_559A_acceptance_1(self):
        mock_input = ['1 1 1 1 1 1']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask559ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_559A_acceptance_2(self):
        mock_input = ['1 2 1 2 1 2']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask559ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

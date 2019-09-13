import unittest
from unittest.mock import patch

from cdf_302A import CodeforcesTask302ASolution


class TestCDF302A(unittest.TestCase):
    def test_302A_acceptance_1(self):
        mock_input = ['2 3', '1 -1', '1 1', '1 2', '2 2']
        expected = '0\n1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask302ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_302A_acceptance_2(self):
        mock_input = ['5 5', '-1 1 1 1 -1', '1 1', '2 3', '3 5', '2 5', '1 5']
        expected = '0\n1\n0\n1\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask302ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

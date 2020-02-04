import unittest
from unittest.mock import patch

from cdf_716A import CodeforcesTask716ASolution


class TestCDF716A(unittest.TestCase):
    def test_716A_acceptance_1(self):
        mock_input = ['6 5', '1 3 8 14 19 20']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask716ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_716A_acceptance_2(self):
        mock_input = ['6 1', '1 3 5 7 9 10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask716ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

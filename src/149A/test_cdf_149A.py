import unittest
from unittest.mock import patch

from cdf_149A import CodeforcesTask149ASolution


class TestCDF149A(unittest.TestCase):
    def test_149A_acceptance_1(self):
        mock_input = ['5', '1 1 1 1 2 2 3 2 2 1 1 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask149ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_149A_acceptance_2(self):
        mock_input = ['0', '0 0 0 0 0 0 0 1 1 2 3 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask149ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_149A_acceptance_3(self):
        mock_input = ['11', '1 1 4 1 1 5 1 1 4 1 1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask149ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

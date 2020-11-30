import unittest
from unittest.mock import patch

from cdf_107A import CodeforcesTask107ASolution


class TestCDF107A(unittest.TestCase):
    def test_107A_acceptance_1(self):
        mock_input = ['3 2', '1 2 10', '2 3 20']
        expected = '1\n1 3 10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask107ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_107A_acceptance_2(self):
        mock_input = ['3 3', '1 2 20', '2 3 10', '3 1 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask107ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_107A_acceptance_3(self):
        mock_input = ['4 2', '1 2 60', '3 4 50']
        expected = '2\n1 2 60\n3 4 50'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask107ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

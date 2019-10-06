import unittest
from unittest.mock import patch

from cdf_911A import CodeforcesTask911ASolution


class TestCDF911A(unittest.TestCase):
    def test_911A_acceptance_1(self):
        mock_input = ['2', '3 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask911ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_911A_acceptance_2(self):
        mock_input = ['3', '5 6 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask911ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_911A_acceptance_3(self):
        mock_input = ['9', '2 1 3 5 4 1 2 3 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask911ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

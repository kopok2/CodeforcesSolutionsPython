import unittest
from unittest.mock import patch

from cdf_863A import CodeforcesTask863ASolution


class TestCDF863A(unittest.TestCase):
    def test_863A_acceptance_1(self):
        mock_input = ['131']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask863ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_863A_acceptance_2(self):
        mock_input = ['320']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask863ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_863A_acceptance_3(self):
        mock_input = ['2010200']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask863ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

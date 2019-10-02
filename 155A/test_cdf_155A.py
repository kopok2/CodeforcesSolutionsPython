import unittest
from unittest.mock import patch

from cdf_155A import CodeforcesTask155ASolution


class TestCDF155A(unittest.TestCase):
    def test_155A_acceptance_1(self):
        mock_input = ['5', '100 50 200 150 200']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask155ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_155A_acceptance_2(self):
        mock_input = ['10', '4664 6496 5814 7010 5762 5736 6944 4850 3698 7242']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask155ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

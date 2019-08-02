import unittest
from unittest.mock import patch

from cdf_90A import CodeforcesTask90ASolution


class TestCDF90A(unittest.TestCase):
    def test_90A_acceptance_1(self):
        mock_input = ['1 3 2']
        expected = '34'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask90ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_90A_acceptance_2(self):
        mock_input = ['3 2 1']
        expected = '33'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask90ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

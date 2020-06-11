import unittest
from unittest.mock import patch

from cdf_657A import CodeforcesTask657ASolution


class TestCDF657A(unittest.TestCase):
    def test_657A_acceptance_1(self):
        mock_input = ['5 3 2']
        expected = '1 2\n1 3\n3 4\n3 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask657ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_657A_acceptance_2(self):
        mock_input = ['8 5 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask657ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_657A_acceptance_3(self):
        mock_input = ['8 4 2']
        expected = '4 8\n5 7\n2 3\n8 1\n2 1\n5 6\n1 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask657ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

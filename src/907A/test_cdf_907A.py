import unittest
from unittest.mock import patch

from cdf_907A import CodeforcesTask907ASolution


class TestCDF907A(unittest.TestCase):
    def test_907A_acceptance_1(self):
        mock_input = ['50 30 10 10']
        expected = '50\n30\n10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask907ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_907A_acceptance_2(self):
        mock_input = ['100 50 10 21']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask907ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

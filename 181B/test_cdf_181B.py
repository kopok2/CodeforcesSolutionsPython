import unittest
from unittest.mock import patch

from cdf_181B import CodeforcesTask181BSolution


class TestCDF181B(unittest.TestCase):
    def test_181B_acceptance_1(self):
        mock_input = ['3', '1 1', '2 2', '3 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask181BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_181B_acceptance_2(self):
        mock_input = ['3', '0 0', '-1 0', '0 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask181BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

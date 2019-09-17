import unittest
from unittest.mock import patch

from cdf_120B import CodeforcesTask120BSolution


class TestCDF120B(unittest.TestCase):
    def test_120B_acceptance_1(self):
        mock_input = ['5 5', '0 1 0 1 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask120BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_120B_acceptance_2(self):
        mock_input = ['2 1', '1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask120BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

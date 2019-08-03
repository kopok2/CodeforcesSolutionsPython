import unittest
from unittest.mock import patch

from cdf_254A import CodeforcesTask254ASolution


class TestCDF254A(unittest.TestCase):
    def test_254A_acceptance_1(self):
        mock_input = ['3', '20 30 10 30 20 10']
        expected = '4 2\n1 5\n6 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask254ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_254A_acceptance_2(self):
        mock_input = ['1', '1 2']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask254ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_504A import CodeforcesTask504ASolution


class TestCDF504A(unittest.TestCase):
    def test_504A_acceptance_1(self):
        mock_input = ['3', '2 3', '1 0', '1 0']
        expected = '2\n1 0\n2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask504ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_504A_acceptance_2(self):
        mock_input = ['2', '1 1', '1 0']
        expected = '1\n0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask504ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

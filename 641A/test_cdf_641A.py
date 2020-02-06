import unittest
from unittest.mock import patch

from cdf_641A import CodeforcesTask641ASolution


class TestCDF641A(unittest.TestCase):
    def test_641A_acceptance_1(self):
        mock_input = ['2', '><', '1 2']
        expected = 'FINITE'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask641ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_641A_acceptance_2(self):
        mock_input = ['3', '>><', '2 1 1']
        expected = 'INFINITE'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask641ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

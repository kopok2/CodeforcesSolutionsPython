import unittest
from unittest.mock import patch

from cdf_613A import CodeforcesTask613ASolution


class TestCDF613A(unittest.TestCase):
    def test_613A_acceptance_1(self):
        mock_input = ['3 0 0', '0 1', '-1 2', '1 2']
        expected = '12.566370614359172464'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask613ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_613A_acceptance_2(self):
        mock_input = ['4 1 -1', '0 0', '1 2', '2 0', '1 1']
        expected = '21.991148575128551812'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask613ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

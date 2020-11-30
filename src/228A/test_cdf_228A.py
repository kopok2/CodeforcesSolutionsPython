import unittest
from unittest.mock import patch

from cdf_228A import CodeforcesTask228ASolution


class TestCDF228A(unittest.TestCase):
    def test_228A_acceptance_1(self):
        mock_input = ['1 7 3 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask228ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_228A_acceptance_2(self):
        mock_input = ['7 7 7 7']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask228ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_285A import CodeforcesTask285ASolution


class TestCDF285A(unittest.TestCase):
    def test_285A_acceptance_1(self):
        mock_input = ['5 2']
        expected = '1 5 2 4 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_285A_acceptance_2(self):
        mock_input = ['3 0']
        expected = '1 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_285A_acceptance_3(self):
        mock_input = ['3 2']
        expected = '3 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask285ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

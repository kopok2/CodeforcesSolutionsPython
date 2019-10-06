import unittest
from unittest.mock import patch

from cdf_166A import CodeforcesTask166ASolution


class TestCDF166A(unittest.TestCase):
    def test_166A_acceptance_1(self):
        mock_input = ['7 2', '4 10', '4 10', '4 10', '3 20', '2 1', '2 1', '1 10']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask166ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_166A_acceptance_2(self):
        mock_input = ['5 4', '3 1', '3 1', '5 3', '3 1', '3 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask166ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

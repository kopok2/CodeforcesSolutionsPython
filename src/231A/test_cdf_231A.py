import unittest
from unittest.mock import patch

from cdf_231A import CodeforcesTask231ASolution


class TestCDF231A(unittest.TestCase):
    def test_231A_acceptance_1(self):
        mock_input = ['3', '1 1 0', '1 1 1', '1 0 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask231ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_231A_acceptance_2(self):
        mock_input = ['2', '1 0 0', '0 1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask231ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

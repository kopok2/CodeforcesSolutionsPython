import unittest
from unittest.mock import patch

from cdf_8A import CodeforcesTask8ASolution


class TestCDF8A(unittest.TestCase):
    def test_8A_acceptance_1(self):
        mock_input = ['atob', 'a', 'b']
        expected = 'forward'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask8ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_8A_acceptance_2(self):
        mock_input = ['aaacaaa', 'aca', 'aa']
        expected = 'both'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask8ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

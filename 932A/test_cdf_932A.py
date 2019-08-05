import unittest
from unittest.mock import patch

from cdf_932A import CodeforcesTask932ASolution


class TestCDF932A(unittest.TestCase):
    def test_932A_acceptance_1(self):
        mock_input = ['aba']
        expected = 'aba'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask932ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_932A_acceptance_2(self):
        mock_input = ['ab']
        expected = 'aabaa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask932ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

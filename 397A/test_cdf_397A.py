import unittest
from unittest.mock import patch

from cdf_397A import CodeforcesTask397ASolution


class TestCDF397A(unittest.TestCase):
    def test_397A_acceptance_1(self):
        mock_input = ['3', '0 5', '2 8', '1 6']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask397ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_397A_acceptance_2(self):
        mock_input = ['3', '0 10', '1 5', '7 15']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask397ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

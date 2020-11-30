import unittest
from unittest.mock import patch

from cdf_237A import CodeforcesTask237ASolution


class TestCDF237A(unittest.TestCase):
    def test_237A_acceptance_1(self):
        mock_input = ['4', '8 0', '8 10', '8 10', '8 45']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask237ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_237A_acceptance_2(self):
        mock_input = ['3', '0 12', '10 11', '22 22']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask237ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

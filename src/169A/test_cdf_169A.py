import unittest
from unittest.mock import patch

from cdf_169A import CodeforcesTask169ASolution


class TestCDF169A(unittest.TestCase):
    def test_169A_acceptance_1(self):
        mock_input = ['5 2 3', '6 2 3 100 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask169ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_169A_acceptance_2(self):
        mock_input = ['7 3 4', '1 1 9 1 1 1 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask169ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

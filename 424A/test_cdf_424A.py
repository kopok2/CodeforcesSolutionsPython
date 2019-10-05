import unittest
from unittest.mock import patch

from cdf_424A import CodeforcesTask424ASolution


class TestCDF424A(unittest.TestCase):
    def test_424A_acceptance_1(self):
        mock_input = ['4', 'xxXx']
        expected = '1\nXxXx'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask424ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_424A_acceptance_2(self):
        mock_input = ['2', 'XX']
        expected = '1\nxX'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask424ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_424A_acceptance_3(self):
        mock_input = ['6', 'xXXxXx']
        expected = '0\nxXXxXx'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask424ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

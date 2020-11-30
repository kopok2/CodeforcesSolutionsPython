import unittest
from unittest.mock import patch

from cdf_679B import CodeforcesTask679BSolution


class TestCDF679B(unittest.TestCase):
    def test_679B_acceptance_1(self):
        mock_input = ['48']
        expected = '9 42'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask679BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_679B_acceptance_2(self):
        mock_input = ['6']
        expected = '6 6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask679BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

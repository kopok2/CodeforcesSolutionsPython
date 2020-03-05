import unittest
from unittest.mock import patch

from cdf_762B import CodeforcesTask762BSolution


class TestCDF762B(unittest.TestCase):
    def test_762B_acceptance_1(self):
        mock_input = ['2 1 1', '4', '5 USB', '6 PS/2', '3 PS/2', '7 PS/2']
        expected = '3 14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask762BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()


import unittest
from unittest.mock import patch

from cdf_20B import CodeforcesTask20BSolution


class TestCDF20B(unittest.TestCase):
    def test_20B_acceptance_1(self):
        mock_input = ['1 -5 6']
        expected = '2\n2.0000000000\n3.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask20BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

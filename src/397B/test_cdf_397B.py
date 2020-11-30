import unittest
from unittest.mock import patch

from cdf_397B import CodeforcesTask397BSolution


class TestCDF397B(unittest.TestCase):
    def test_397B_acceptance_1(self):
        mock_input = ['2', '5 2 3', '6 4 5']
        expected = 'Yes\nNo'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask397BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

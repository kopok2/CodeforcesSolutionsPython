import unittest
from unittest.mock import patch

from cdf_23B import CodeforcesTask23BSolution


class TestCDF23B(unittest.TestCase):
    def test_23B_acceptance_1(self):
        mock_input = ['1', '3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask23BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_749B import CodeforcesTask749BSolution


class TestCDF749B(unittest.TestCase):
    def test_749B_acceptance_1(self):
        mock_input = ['0 0', '1 0', '0 1']
        expected = '3\n1 -1\n-1 1\n1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask749BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

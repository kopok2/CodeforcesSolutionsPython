import unittest
from unittest.mock import patch

from cdf_139B import CodeforcesTask139BSolution


class TestCDF139B(unittest.TestCase):
    def test_139B_acceptance_1(self):
        mock_input = ['1', '5 5 3', '3', '10 1 100', '15 2 320', '3 19 500']
        expected = '640'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask139BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

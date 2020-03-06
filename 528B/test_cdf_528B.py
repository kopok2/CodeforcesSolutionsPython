import unittest
from unittest.mock import patch

from cdf_528B import CodeforcesTask528BSolution


class TestCDF528B(unittest.TestCase):
    def test_528B_acceptance_1(self):
        mock_input = ['4', '2 3', '3 1', '6 1', '0 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask528BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

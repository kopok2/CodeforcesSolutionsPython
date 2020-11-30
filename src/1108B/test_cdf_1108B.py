import unittest
from unittest.mock import patch

from cdf_1108B import CodeforcesTask1108BSolution


class TestCDF1108B(unittest.TestCase):
    def test_1108B_acceptance_1(self):
        mock_input = ['10 10 2 8 1 2 4 1 20 4 5']
        expected = '20 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1108BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_416B import CodeforcesTask416BSolution


class TestCDF416B(unittest.TestCase):
    def test_416B_acceptance_1(self):
        mock_input = ['5 1', '1', '2', '3', '4', '5']
        expected = '1 3 6 10 15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask416BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_416B_acceptance_2(self):
        mock_input = ['4 2', '2 5', '3 1', '5 3', '10 1']
        expected = '7 8 13 21'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask416BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

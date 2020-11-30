import unittest
from unittest.mock import patch

from cdf_981B import CodeforcesTask981BSolution


class TestCDF981B(unittest.TestCase):
    def test_981B_acceptance_1(self):
        mock_input = ['3', '1 2', '7 2', '3 10', '4', '1 4', '2 4', '3 4', '4 4']
        expected = '24'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask981BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_981B_acceptance_2(self):
        mock_input = ['1', '1000000000 239', '3', '14 15', '92 65', '35 89']
        expected = '408'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask981BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

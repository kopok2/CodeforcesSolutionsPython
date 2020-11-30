import unittest
from unittest.mock import patch

from cdf_268B import CodeforcesTask268BSolution


class TestCDF268B(unittest.TestCase):
    def test_268B_acceptance_1(self):
        mock_input = ['2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask268BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_268B_acceptance_2(self):
        mock_input = ['3']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask268BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

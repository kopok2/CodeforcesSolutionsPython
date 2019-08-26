import unittest
from unittest.mock import patch

from cdf_242B import CodeforcesTask242BSolution


class TestCDF242B(unittest.TestCase):
    def test_242B_acceptance_1(self):
        mock_input = ['3', '1 1', '2 2', '3 3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask242BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_242B_acceptance_2(self):
        mock_input = ['6', '1 5', '2 3', '1 10', '7 10', '7 7', '10 10']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask242BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

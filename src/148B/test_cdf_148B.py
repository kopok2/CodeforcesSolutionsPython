import unittest
from unittest.mock import patch

from cdf_148B import CodeforcesTask148BSolution


class TestCDF148B(unittest.TestCase):
    def test_148B_acceptance_1(self):
        mock_input = ['1', '2', '1', '1', '10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask148BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_148B_acceptance_2(self):
        mock_input = ['1', '2', '1', '1', '8']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask148BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

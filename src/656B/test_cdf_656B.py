import unittest
from unittest.mock import patch

from cdf_656B import CodeforcesTask656BSolution


class TestCDF656B(unittest.TestCase):
    def test_656B_acceptance_1(self):
        mock_input = ['1', '2', '0']
        expected = '0.500000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask656BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_656B_acceptance_2(self):
        mock_input = ['2', '2 3', '1 0']
        expected = '0.666667'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask656BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1027B import CodeforcesTask1027BSolution


class TestCDF1027B(unittest.TestCase):
    def test_1027B_acceptance_1(self):
        mock_input = ['4 5', '1 1', '4 4', '4 3', '3 2', '2 4']
        expected = '1\n8\n16\n13\n4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1027BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1027B_acceptance_2(self):
        mock_input = ['5 4', '2 1', '4 2', '3 3', '3 4']
        expected = '16\n9\n7\n20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1027BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

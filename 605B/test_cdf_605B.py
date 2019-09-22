import unittest
from unittest.mock import patch

from cdf_605B import CodeforcesTask605BSolution


class TestCDF605B(unittest.TestCase):
    def test_605B_acceptance_1(self):
        mock_input = ['4 5', '2 1', '3 1', '4 0', '1 1', '5 0']
        expected = '2 4\n1 4\n3 4\n3 1\n3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask605BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_605B_acceptance_2(self):
        mock_input = ['3 3', '1 0', '2 1', '3 1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask605BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

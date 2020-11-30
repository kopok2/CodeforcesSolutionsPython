import unittest
from unittest.mock import patch

from cdf_432B import CodeforcesTask432BSolution


class TestCDF432B(unittest.TestCase):
    def test_432B_acceptance_1(self):
        mock_input = ['2', '1 2', '2 1']
        expected = '2 0\n2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask432BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_432B_acceptance_2(self):
        mock_input = ['3', '1 2', '2 1', '1 3']
        expected = '3 1\n4 0\n2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask432BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

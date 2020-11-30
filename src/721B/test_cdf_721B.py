import unittest
from unittest.mock import patch

from cdf_721B import CodeforcesTask721BSolution


class TestCDF721B(unittest.TestCase):
    def test_721B_acceptance_1(self):
        mock_input = ['5 2', 'cba', 'abc', 'bb1', 'abC', 'ABC', 'abc']
        expected = '1 15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask721BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_721B_acceptance_2(self):
        mock_input = ['4 100', '11', '22', '1', '2', '22']
        expected = '3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask721BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

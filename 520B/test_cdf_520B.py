import unittest
from unittest.mock import patch

from cdf_520B import CodeforcesTask520BSolution


class TestCDF520B(unittest.TestCase):
    def test_520B_acceptance_1(self):
        mock_input = ['4 6']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask520BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_520B_acceptance_2(self):
        mock_input = ['10 1']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask520BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

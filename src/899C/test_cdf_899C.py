import unittest
from unittest.mock import patch

from cdf_899C import CodeforcesTask899CSolution


class TestCDF899C(unittest.TestCase):
    def test_899C_acceptance_1(self):
        mock_input = ['4']
        expected = '0\n2 1 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask899CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_899C_acceptance_2(self):
        mock_input = ['2']
        expected = '1\n1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask899CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

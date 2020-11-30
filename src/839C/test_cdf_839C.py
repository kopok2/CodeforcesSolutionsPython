import unittest
from unittest.mock import patch

from cdf_839C import CodeforcesTask839CSolution


class TestCDF839C(unittest.TestCase):
    def test_839C_acceptance_1(self):
        mock_input = ['4', '1 2', '1 3', '2 4']
        expected = '1.500000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask839CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_839C_acceptance_2(self):
        mock_input = ['5', '1 2', '1 3', '3 4', '2 5']
        expected = '2.000000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask839CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

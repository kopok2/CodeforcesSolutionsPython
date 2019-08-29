import unittest
from unittest.mock import patch

from cdf_313B import CodeforcesTask313BSolution


class TestCDF313B(unittest.TestCase):
    def test_313B_acceptance_1(self):
        mock_input = ['......', '4', '3 4', '2 3', '1 6', '2 6']
        expected = '1\n1\n5\n4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask313BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_313B_acceptance_2(self):
        mock_input = ['#..###', '5', '1 3', '5 6', '1 5', '3 6', '3 4']
        expected = '1\n1\n2\n2\n0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask313BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

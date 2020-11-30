import unittest
from unittest.mock import patch

from cdf_847B import CodeforcesTask847BSolution


class TestCDF847B(unittest.TestCase):
    def test_847B_acceptance_1(self):
        mock_input = ['5', '1 3 2 5 4']
        expected = '1 3 5\n2 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask847BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_847B_acceptance_2(self):
        mock_input = ['4', '4 3 2 1']
        expected = '4\n3\n2\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask847BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_847B_acceptance_3(self):
        mock_input = ['4', '10 30 50 101']
        expected = '10 30 50 101'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask847BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

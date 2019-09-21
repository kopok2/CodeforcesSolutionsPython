import unittest
from unittest.mock import patch

from cdf_1139B import CodeforcesTask1139BSolution


class TestCDF1139B(unittest.TestCase):
    def test_1139B_acceptance_1(self):
        mock_input = ['5 1 2 1 3 6']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1139BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1139B_acceptance_2(self):
        mock_input = ['5 3 2 5 4 10']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1139BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1139B_acceptance_3(self):
        mock_input = ['4 1 1 1 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1139BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

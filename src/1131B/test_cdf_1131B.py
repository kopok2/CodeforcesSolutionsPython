import unittest
from unittest.mock import patch

from cdf_1131B import CodeforcesTask1131BSolution


class TestCDF1131B(unittest.TestCase):
    def test_1131B_acceptance_1(self):
        mock_input = ['3', '2 0', '3 1', '3 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1131BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1131B_acceptance_2(self):
        mock_input = ['3', '0 0', '0 0', '0 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1131BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1131B_acceptance_3(self):
        mock_input = ['1', '5 4']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1131BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1073B import CodeforcesTask1073BSolution


class TestCDF1073B(unittest.TestCase):
    def test_1073B_acceptance_1(self):
        mock_input = ['3', '1 2 3', '2 1 3']
        expected = '2 0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1073BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1073B_acceptance_2(self):
        mock_input = ['5', '3 1 4 2 5', '4 5 1 3 2']
        expected = '3 2 0 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1073BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1073B_acceptance_3(self):
        mock_input = ['6', '6 5 4 3 2 1', '6 5 3 4 2 1']
        expected = '1 1 2 0 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1073BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

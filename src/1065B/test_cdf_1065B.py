import unittest
from unittest.mock import patch

from cdf_1065B import CodeforcesTask1065BSolution


class TestCDF1065B(unittest.TestCase):
    def test_1065B_acceptance_1(self):
        mock_input = ['4 2']
        expected = '0 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1065BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1065B_acceptance_2(self):
        mock_input = ['3 1']
        expected = '1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1065BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

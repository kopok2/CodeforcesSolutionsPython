import unittest
from unittest.mock import patch

from cdf_1099B import CodeforcesTask1099BSolution


class TestCDF1099B(unittest.TestCase):
    def test_1099B_acceptance_1(self):
        mock_input = ['1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1099BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1099B_acceptance_2(self):
        mock_input = ['2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1099BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1099B_acceptance_3(self):
        mock_input = ['4']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1099BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

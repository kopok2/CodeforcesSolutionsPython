import unittest
from unittest.mock import patch

from cdf_286B import CodeforcesTask286BSolution


class TestCDF286B(unittest.TestCase):
    def test_286B_acceptance_1(self):
        mock_input = ['2']
        expected = '2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask286BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_286B_acceptance_2(self):
        mock_input = ['3']
        expected = '1 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask286BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_286B_acceptance_3(self):
        mock_input = ['4']
        expected = '4 2 3 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask286BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

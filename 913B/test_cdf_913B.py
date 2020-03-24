import unittest
from unittest.mock import patch

from cdf_913B import CodeforcesTask913BSolution


class TestCDF913B(unittest.TestCase):
    def test_913B_acceptance_1(self):
        mock_input = ['4', '1', '1', '1']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask913BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_913B_acceptance_2(self):
        mock_input = ['7', '1', '1', '1', '2', '2', '2']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask913BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_913B_acceptance_3(self):
        mock_input = ['8', '1', '1', '1', '1', '3', '3', '3']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask913BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

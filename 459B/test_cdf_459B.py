import unittest
from unittest.mock import patch

from cdf_459B import CodeforcesTask459BSolution


class TestCDF459B(unittest.TestCase):
    def test_459B_acceptance_1(self):
        mock_input = ['2', '1 2']
        expected = '1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_459B_acceptance_2(self):
        mock_input = ['3', '1 4 5']
        expected = '4 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_459B_acceptance_3(self):
        mock_input = ['5', '3 1 2 3 1']
        expected = '2 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask459BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

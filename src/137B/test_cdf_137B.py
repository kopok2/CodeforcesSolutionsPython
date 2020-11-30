import unittest
from unittest.mock import patch

from cdf_137B import CodeforcesTask137BSolution


class TestCDF137B(unittest.TestCase):
    def test_137B_acceptance_1(self):
        mock_input = ['3', '3 1 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask137BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_137B_acceptance_2(self):
        mock_input = ['2', '2 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask137BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_137B_acceptance_3(self):
        mock_input = ['5', '5 3 3 3 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask137BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

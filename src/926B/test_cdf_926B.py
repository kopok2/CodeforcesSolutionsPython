import unittest
from unittest.mock import patch

from cdf_926B import CodeforcesTask926BSolution


class TestCDF926B(unittest.TestCase):
    def test_926B_acceptance_1(self):
        mock_input = ['3', '-5 10 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_926B_acceptance_2(self):
        mock_input = ['6', '100 200 400 300 600 500']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_926B_acceptance_3(self):
        mock_input = ['4', '10 9 0 -1']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

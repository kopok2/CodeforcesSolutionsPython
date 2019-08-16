import unittest
from unittest.mock import patch

from cdf_557B import CodeforcesTask557BSolution


class TestCDF557B(unittest.TestCase):
    def test_557B_acceptance_1(self):
        mock_input = ['2 4', '1 1 1 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask557BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_557B_acceptance_2(self):
        mock_input = ['3 18', '4 4 4 2 2 2']
        expected = '18'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask557BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_557B_acceptance_3(self):
        mock_input = ['1 5', '2 3']
        expected = '4.5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask557BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

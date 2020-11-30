import unittest
from unittest.mock import patch

from cdf_394B import CodeforcesTask394BSolution


class TestCDF394B(unittest.TestCase):
    def test_394B_acceptance_1(self):
        mock_input = ['6 5']
        expected = '142857'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_394B_acceptance_2(self):
        mock_input = ['1 2']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_394B_acceptance_3(self):
        mock_input = ['6 4']
        expected = '102564'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

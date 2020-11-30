import unittest
from unittest.mock import patch

from cdf_525B import CodeforcesTask525BSolution


class TestCDF525B(unittest.TestCase):
    def test_525B_acceptance_1(self):
        mock_input = ['abcdef', '1', '2']
        expected = 'aedcbf'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_525B_acceptance_2(self):
        mock_input = ['vwxyz', '2', '2 2']
        expected = 'vwxyz'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_525B_acceptance_3(self):
        mock_input = ['abcdef', '3', '1 2 3']
        expected = 'fbdcea'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask525BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

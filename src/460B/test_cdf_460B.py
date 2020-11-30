import unittest
from unittest.mock import patch

from cdf_460B import CodeforcesTask460BSolution


class TestCDF460B(unittest.TestCase):
    def test_460B_acceptance_1(self):
        mock_input = ['3 2 8']
        expected = '3\n10 2008 13726'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask460BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_460B_acceptance_2(self):
        mock_input = ['1 2 -18']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask460BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_460B_acceptance_3(self):
        mock_input = ['2 2 -1']
        expected = '4\n1 31 337 967'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask460BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

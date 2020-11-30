import unittest
from unittest.mock import patch

from cdf_807B import CodeforcesTask807BSolution


class TestCDF807B(unittest.TestCase):
    def test_807B_acceptance_1(self):
        mock_input = ['239 10880 9889']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask807BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_807B_acceptance_2(self):
        mock_input = ['26 7258 6123']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask807BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_807B_acceptance_3(self):
        mock_input = ['493 8000 8000']
        expected = '24'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask807BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_807B_acceptance_4(self):
        mock_input = ['101 6800 6500']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask807BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_807B_acceptance_5(self):
        mock_input = ['329 19913 19900']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask807BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

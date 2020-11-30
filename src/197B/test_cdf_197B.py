import unittest
from unittest.mock import patch

from cdf_197B import CodeforcesTask197BSolution


class TestCDF197B(unittest.TestCase):
    def test_197B_acceptance_1(self):
        mock_input = ['2 1', '1 1 1', '2 5']
        expected = 'Infinity'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask197BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_197B_acceptance_2(self):
        mock_input = ['1 0', '-1 3', '2']
        expected = '-Infinity'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask197BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_197B_acceptance_3(self):
        mock_input = ['0 1', '1', '1 0']
        expected = '0/1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask197BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_197B_acceptance_4(self):
        mock_input = ['2 2', '2 1 6', '4 5 -7']
        expected = '1/2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask197BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_197B_acceptance_5(self):
        mock_input = ['1 1', '9 0', '-5 2']
        expected = '-9/5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask197BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

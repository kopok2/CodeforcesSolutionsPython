import unittest
from unittest.mock import patch

from cdf_798B import CodeforcesTask798BSolution


class TestCDF798B(unittest.TestCase):
    def test_798B_acceptance_1(self):
        mock_input = ['4', 'xzzwo', 'zwoxz', 'zzwox', 'xzzwo']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask798BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_798B_acceptance_2(self):
        mock_input = ['2', 'molzv', 'lzvmo']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask798BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_798B_acceptance_3(self):
        mock_input = ['3', 'kc', 'kc', 'kc']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask798BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_798B_acceptance_4(self):
        mock_input = ['3', 'aa', 'aa', 'ab']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask798BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

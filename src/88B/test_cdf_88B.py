import unittest
from unittest.mock import patch

from cdf_88B import CodeforcesTask88BSolution


class TestCDF88B(unittest.TestCase):
    def test_88B_acceptance_1(self):
        mock_input = ['2 2 1', 'ab', 'cd', '1', 'A']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask88BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_88B_acceptance_2(self):
        mock_input = ['2 2 1', 'ab', 'cd', '1', 'e']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask88BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_88B_acceptance_3(self):
        mock_input = ['2 2 1', 'ab', 'cS', '5', 'abcBA']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask88BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_88B_acceptance_4(self):
        mock_input = ['3 9 4', 'qwertyuio', 'asdfghjkl', 'SzxcvbnmS', '35', 'TheQuIcKbRoWnFOXjummsovertHeLazYDOG']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask88BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

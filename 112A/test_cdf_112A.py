import unittest
from unittest.mock import patch

from cdf_112A import CodeforcesTask112ASolution


class TestCDF112A(unittest.TestCase):
    def test_112A_acceptance_1(self):
        mock_input = ['aaaa', 'aaaA']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask112ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_112A_acceptance_2(self):
        mock_input = ['abs', 'Abz']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask112ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_112A_acceptance_3(self):
        mock_input = ['abcdefg', 'AbCdEfF']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask112ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

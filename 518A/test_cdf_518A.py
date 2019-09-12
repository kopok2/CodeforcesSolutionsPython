import unittest
from unittest.mock import patch

from cdf_518A import CodeforcesTask518ASolution


class TestCDF518A(unittest.TestCase):
    def test_518A_acceptance_1(self):
        mock_input = ['a', 'c']
        expected = 'b'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_518A_acceptance_2(self):
        mock_input = ['aaa', 'zzz']
        expected = 'kkk'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_518A_acceptance_3(self):
        mock_input = ['abcdefg', 'abcdefh']
        expected = 'No such string'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask518ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_101A import CodeforcesTask101ASolution


class TestCDF101A(unittest.TestCase):
    def test_101A_acceptance_1(self):
        mock_input = ['aaaaa', '4']
        expected = '1\naaaaa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask101ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_101A_acceptance_2(self):
        mock_input = ['abacaba', '4']
        expected = '1\naaaa'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask101ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_101A_acceptance_3(self):
        mock_input = ['abcdefgh', '10']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask101ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

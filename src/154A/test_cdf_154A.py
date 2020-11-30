import unittest
from unittest.mock import patch

from cdf_154A import CodeforcesTask154ASolution


class TestCDF154A(unittest.TestCase):
    def test_154A_acceptance_1(self):
        mock_input = ['ababa', '1', 'ab']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask154ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_154A_acceptance_2(self):
        mock_input = ['codeforces', '2', 'do', 'cs']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask154ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

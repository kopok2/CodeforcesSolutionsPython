import unittest
from unittest.mock import patch

from cdf_947A import CodeforcesTask947ASolution


class TestCDF947A(unittest.TestCase):
    def test_947A_acceptance_1(self):
        mock_input = ['14']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask947ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_947A_acceptance_2(self):
        mock_input = ['20']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask947ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_947A_acceptance_3(self):
        mock_input = ['8192']
        expected = '8191'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask947ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

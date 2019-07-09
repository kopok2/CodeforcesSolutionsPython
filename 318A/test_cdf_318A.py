import unittest
from unittest.mock import patch

from cdf_318A import CodeforcesTask318ASolution


class TestCDF3B(unittest.TestCase):
    def test_318A_acceptance_1(self):
        mock_input = ['10 3']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask318ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_318A_acceptance_2(self):
        mock_input = ['7 7']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask318ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

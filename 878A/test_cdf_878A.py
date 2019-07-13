import unittest
from unittest.mock import patch

from cdf_878A import CodeforcesTask878ASolution


class TestCDF878A(unittest.TestCase):
    def test_878A_acceptance_1(self):
        mock_input = ['3', '| 3', '^ 2', '| 1']
        expected = '2\n| 3\n^ 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask878ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_878A_acceptance_2(self):
        mock_input = ['3', '& 1', '& 3', '& 5']
        expected = '1\n& 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask878ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_878A_acceptance_3(self):
        mock_input = ['3', '^ 1', '^ 2', '^ 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask878ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

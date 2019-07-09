import unittest
from unittest.mock import patch

from cdf_257A import CodeforcesTask257ASolution


class TestCDF257A(unittest.TestCase):
    def test_257A_acceptance_1(self):
        mock_input = ['3 5 3', '3 1 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask257ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_257A_acceptance_2(self):
        mock_input = ['4 7 2', '3 3 2 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask257ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_257A_acceptance_3(self):
        mock_input = ['5 5 1', '1 3 1 2 1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask257ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

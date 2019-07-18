import unittest
from unittest.mock import patch

from cdf_931A import CodeforcesTask931ASolution


class TestCDF931A(unittest.TestCase):
    def test_931A_acceptance_1(self):
        mock_input = ['3', '4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_931A_acceptance_2(self):
        mock_input = ['101', '99']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_931A_acceptance_3(self):
        mock_input = ['5', '10']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask931ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

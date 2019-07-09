import unittest
from unittest.mock import patch

from cdf_187A import CodeforcesTask187ASolution


class TestCDF187A(unittest.TestCase):
    def test_187A_acceptance_1(self):
        mock_input = ['3', '3 2 1', '1 2 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask187ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_187A_acceptance_2(self):
        mock_input = ['5', '1 2 3 4 5', '1 5 2 3 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask187ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_187A_acceptance_3(self):
        mock_input = ['5', '1 5 2 3 4', '1 2 3 4 5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask187ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

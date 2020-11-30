import unittest
from unittest.mock import patch

from cdf_585A import CodeforcesTask585ASolution


class TestCDF585A(unittest.TestCase):
    def test_585A_acceptance_1(self):
        mock_input = ['5', '4 2 2', '4 1 2', '5 2 4', '3 3 5', '5 1 2']
        expected = '2\n1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask585ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_585A_acceptance_2(self):
        mock_input = ['5', '4 5 1', '5 3 9', '4 1 2', '2 1 8', '4 1 9']
        expected = '4\n1 2 4 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask585ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

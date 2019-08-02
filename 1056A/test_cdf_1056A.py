import unittest
from unittest.mock import patch

from cdf_1056A import CodeforcesTask1056ASolution


class TestCDF1056A(unittest.TestCase):
    def test_1056A_acceptance_1(self):
        mock_input = ['3 3 1 4 6 2 1 4 5 10 5 6 4 1']
        expected = '1 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1056ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1056A_acceptance_2(self):
        mock_input = ['5 1 1 10 10 9 8 7 100 5 4 3 99 1 5 1 2 3 4 5 5 4 1 3 2 5 4 10 1 5 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1056ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1006A import CodeforcesTask1006ASolution


class TestCDF1006A(unittest.TestCase):
    def test_1006A_acceptance_1(self):
        mock_input = ['5', '1 2 4 5 10']
        expected = '1 1 3 5 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1006A_acceptance_2(self):
        mock_input = ['10', '10000 10 50605065 1 5 89 5 999999999 60506056 1000000000']
        expected = '9999 9 50605065 1 5 89 5 999999999 60506055 999999999'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1043A import CodeforcesTask1043ASolution


class TestCDF1043A(unittest.TestCase):
    def test_1043A_acceptance_1(self):
        mock_input = ['5', '1 1 1 5 1']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1043ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1043A_acceptance_2(self):
        mock_input = ['5', '2 2 3 2 2']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1043ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

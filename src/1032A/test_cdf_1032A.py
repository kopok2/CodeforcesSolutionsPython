import unittest
from unittest.mock import patch

from cdf_1032A import CodeforcesTask1032ASolution


class TestCDF1032A(unittest.TestCase):
    def test_1032A_acceptance_1(self):
        mock_input = ['5 2 1 2 2 1 3']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1032ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1032A_acceptance_2(self):
        mock_input = ['10 3 1 3 3 1 3 5 5 5 5 100']
        expected = '14'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1032ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

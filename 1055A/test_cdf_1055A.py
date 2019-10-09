import unittest
from unittest.mock import patch

from cdf_1055A import CodeforcesTask1055ASolution


class TestCDF1055A(unittest.TestCase):
    def test_1055A_acceptance_1(self):
        mock_input = ['5 3', '1 1 1 1 1', '1 1 1 1 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1055ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1055A_acceptance_2(self):
        mock_input = ['5 4', '1 0 0 0 1', '0 1 1 1 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1055ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1055A_acceptance_3(self):
        mock_input = ['5 2', '0 1 1 1 1', '1 1 1 1 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1055ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

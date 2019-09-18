import unittest
from unittest.mock import patch

from cdf_1119A import CodeforcesTask1119ASolution


class TestCDF1119A(unittest.TestCase):
    def test_1119A_acceptance_1(self):
        mock_input = ['5 1 2 3 2 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1119ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1119A_acceptance_2(self):
        mock_input = ['3 1 2 1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1119ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1119A_acceptance_3(self):
        mock_input = ['7 1 1 3 1 1 1 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1119ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

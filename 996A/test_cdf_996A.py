import unittest
from unittest.mock import patch

from cdf_996A import CodeforcesTask996ASolution


class TestCDF996A(unittest.TestCase):
    def test_996A_acceptance_1(self):
        mock_input = ['125']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask996ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_996A_acceptance_2(self):
        mock_input = ['43']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask996ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_996A_acceptance_3(self):
        mock_input = ['1000000000']
        expected = '10000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask996ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

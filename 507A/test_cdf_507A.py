import unittest
from unittest.mock import patch

from cdf_507A import CodeforcesTask507ASolution


class TestCDF507A(unittest.TestCase):
    def test_507A_acceptance_1(self):
        mock_input = ['4 10', '4 3 1 2']
        expected = '4\n1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask507ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_507A_acceptance_2(self):
        mock_input = ['5 6', '4 3 1 1 2']
        expected = '3\n1 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask507ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_507A_acceptance_3(self):
        mock_input = ['1 3', '4']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask507ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

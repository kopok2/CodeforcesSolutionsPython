import unittest
from unittest.mock import patch

from cdf_749A import CodeforcesTask749ASolution


class TestCDF749A(unittest.TestCase):
    def test_749A_acceptance_1(self):
        mock_input = ['5']
        expected = '2\n2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask749ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_749A_acceptance_2(self):
        mock_input = ['6']
        expected = '3\n2 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask749ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

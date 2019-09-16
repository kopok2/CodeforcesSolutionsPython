import unittest
from unittest.mock import patch

from cdf_355A import CodeforcesTask355ASolution


class TestCDF355A(unittest.TestCase):
    def test_355A_acceptance_1(self):
        mock_input = ['4 4']
        expected = '5881'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask355ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_355A_acceptance_2(self):
        mock_input = ['5 1']
        expected = '36172'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask355ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_355A_acceptance_3(self):
        mock_input = ['1 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask355ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_750A import CodeforcesTask750ASolution


class TestCDF750A(unittest.TestCase):
    def test_750A_acceptance_1(self):
        mock_input = ['3 222']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask750ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_750A_acceptance_2(self):
        mock_input = ['4 190']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask750ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_750A_acceptance_3(self):
        mock_input = ['7 1']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask750ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

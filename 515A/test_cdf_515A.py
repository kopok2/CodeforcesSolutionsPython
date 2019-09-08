import unittest
from unittest.mock import patch

from cdf_515A import CodeforcesTask515ASolution


class TestCDF515A(unittest.TestCase):
    def test_515A_acceptance_1(self):
        mock_input = ['5 5 11']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask515ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_515A_acceptance_2(self):
        mock_input = ['10 15 25']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask515ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_515A_acceptance_3(self):
        mock_input = ['0 5 1']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask515ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_515A_acceptance_4(self):
        mock_input = ['0 0 2']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask515ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

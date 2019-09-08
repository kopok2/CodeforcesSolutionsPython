import unittest
from unittest.mock import patch

from cdf_321A import CodeforcesTask321ASolution


class TestCDF321A(unittest.TestCase):
    def test_321A_acceptance_1(self):
        mock_input = ['2 2', 'RU']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask321ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_321A_acceptance_2(self):
        mock_input = ['1 2', 'RU']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask321ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_321A_acceptance_3(self):
        mock_input = ['-1 1000000000', 'LRRLU']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask321ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_321A_acceptance_4(self):
        mock_input = ['0 0', 'D']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask321ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

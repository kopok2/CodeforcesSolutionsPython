import unittest
from unittest.mock import patch

from cdf_803A import CodeforcesTask803ASolution


class TestCDF803A(unittest.TestCase):
    def test_803A_acceptance_1(self):
        mock_input = ['2 1']
        expected = '1 0\n0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_803A_acceptance_2(self):
        mock_input = ['3 2']
        expected = '1 0 0\n0 1 0\n0 0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_803A_acceptance_3(self):
        mock_input = ['2 5']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

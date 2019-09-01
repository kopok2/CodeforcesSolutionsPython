import unittest
from unittest.mock import patch

from cdf_1038A import CodeforcesTask1038ASolution


class TestCDF1038A(unittest.TestCase):
    def test_1038A_acceptance_1(self):
        mock_input = ['9 3', 'ACAABCCAB']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1038ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1038A_acceptance_2(self):
        mock_input = ['9 4', 'ABCABCABC']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1038ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

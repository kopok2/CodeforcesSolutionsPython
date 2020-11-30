import unittest
from unittest.mock import patch

from cdf_766A import CodeforcesTask766ASolution


class TestCDF766A(unittest.TestCase):
    def test_766A_acceptance_1(self):
        mock_input = ['abcd', 'defgh']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask766ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_766A_acceptance_2(self):
        mock_input = ['a', 'a']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask766ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

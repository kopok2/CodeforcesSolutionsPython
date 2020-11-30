import unittest
from unittest.mock import patch

from cdf_805A import CodeforcesTask805ASolution


class TestCDF805A(unittest.TestCase):
    def test_805A_acceptance_1(self):
        mock_input = ['19 29']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask805ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_805A_acceptance_2(self):
        mock_input = ['3 6']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask805ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

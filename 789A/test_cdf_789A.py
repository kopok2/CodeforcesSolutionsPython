import unittest
from unittest.mock import patch

from cdf_789A import CodeforcesTask789ASolution


class TestCDF789A(unittest.TestCase):
    def test_789A_acceptance_1(self):
        mock_input = ['3 2', '2 3 4']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask789ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_789A_acceptance_2(self):
        mock_input = ['5 4', '3 1 8 9 7']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask789ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

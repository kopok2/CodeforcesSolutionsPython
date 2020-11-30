import unittest
from unittest.mock import patch

from cdf_37A import CodeforcesTask37ASolution


class TestCDF37A(unittest.TestCase):
    def test_37A_acceptance_1(self):
        mock_input = ['3', '1 2 3']
        expected = '1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask37ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_37A_acceptance_2(self):
        mock_input = ['4', '6 5 6 7']
        expected = '2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask37ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

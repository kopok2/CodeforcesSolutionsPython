import unittest
from unittest.mock import patch

from cdf_134A import CodeforcesTask134ASolution


class TestCDF134A(unittest.TestCase):
    def test_134A_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '1\n3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask134ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_134A_acceptance_2(self):
        mock_input = ['4', '50 50 50 50']
        expected = '4\n1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask134ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_761A import CodeforcesTask761ASolution


class TestCDF761A(unittest.TestCase):
    def test_761A_acceptance_1(self):
        mock_input = ['2 3']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask761ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_761A_acceptance_2(self):
        mock_input = ['3 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask761ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

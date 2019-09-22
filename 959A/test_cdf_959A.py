import unittest
from unittest.mock import patch

from cdf_959A import CodeforcesTask959ASolution


class TestCDF959A(unittest.TestCase):
    def test_959A_acceptance_1(self):
        mock_input = ['1']
        expected = 'Ehab'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask959ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_959A_acceptance_2(self):
        mock_input = ['2']
        expected = 'Mahmoud'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask959ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

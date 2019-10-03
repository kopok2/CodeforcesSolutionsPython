import unittest
from unittest.mock import patch

from cdf_282A import CodeforcesTask282ASolution


class TestCDF282A(unittest.TestCase):
    def test_282A_acceptance_1(self):
        mock_input = ['1', '++X']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask282ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_282A_acceptance_2(self):
        mock_input = ['2', 'X++', '--X']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask282ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

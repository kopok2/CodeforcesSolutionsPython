import unittest
from unittest.mock import patch

from cdf_217A import CodeforcesTask217ASolution


class TestCDF217A(unittest.TestCase):
    def test_217A_acceptance_1(self):
        mock_input = ['2', '2 1', '1 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask217ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_217A_acceptance_2(self):
        mock_input = ['2', '2 1', '4 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask217ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

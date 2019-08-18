import unittest
from unittest.mock import patch

from cdf_914A import CodeforcesTask914ASolution


class TestCDF914A(unittest.TestCase):
    def test_914A_acceptance_1(self):
        mock_input = ['2', '4 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask914ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_914A_acceptance_2(self):
        mock_input = ['8', '1 2 4 8 16 32 64 576']
        expected = '32'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask914ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

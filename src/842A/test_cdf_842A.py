import unittest
from unittest.mock import patch

from cdf_842A import CodeforcesTask842ASolution


class TestCDF842A(unittest.TestCase):
    def test_842A_acceptance_1(self):
        mock_input = ['1 10 1 10 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask842ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_842A_acceptance_2(self):
        mock_input = ['1 5 6 10 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask842ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

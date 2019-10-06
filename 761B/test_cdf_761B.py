import unittest
from unittest.mock import patch

from cdf_761B import CodeforcesTask761BSolution


class TestCDF761B(unittest.TestCase):
    def test_761B_acceptance_1(self):
        mock_input = ['3 8', '2 4 6', '1 5 7']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask761BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_761B_acceptance_2(self):
        mock_input = ['4 9', '2 3 5 8', '0 1 3 6']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask761BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_761B_acceptance_3(self):
        mock_input = ['2 4', '1 3', '1 2']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask761BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

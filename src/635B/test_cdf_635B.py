import unittest
from unittest.mock import patch

from cdf_635B import CodeforcesTask635BSolution


class TestCDF635B(unittest.TestCase):
    def test_635B_acceptance_1(self):
        mock_input = ['3', '1 0 2', '2 0 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask635BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_635B_acceptance_2(self):
        mock_input = ['2', '1 0', '0 1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask635BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_635B_acceptance_3(self):
        mock_input = ['4', '1 2 3 0', '0 3 2 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask635BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

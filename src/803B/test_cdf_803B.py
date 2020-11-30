import unittest
from unittest.mock import patch

from cdf_803B import CodeforcesTask803BSolution


class TestCDF803B(unittest.TestCase):
    def test_803B_acceptance_1(self):
        mock_input = ['9', '2 1 0 3 0 0 3 2 4']
        expected = '2 1 0 1 0 0 1 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_803B_acceptance_2(self):
        mock_input = ['5', '0 1 2 3 4']
        expected = '0 1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_803B_acceptance_3(self):
        mock_input = ['7', '5 6 0 1 -2 3 4']
        expected = '2 1 0 1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask803BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

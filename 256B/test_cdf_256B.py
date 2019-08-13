import unittest
from unittest.mock import patch

from cdf_256B import CodeforcesTask256BSolution


class TestCDF256B(unittest.TestCase):
    def test_256B_acceptance_1(self):
        mock_input = ['6 4 3 1']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask256BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_256B_acceptance_2(self):
        mock_input = ['9 3 8 10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask256BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

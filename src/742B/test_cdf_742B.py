import unittest
from unittest.mock import patch

from cdf_742B import CodeforcesTask742BSolution


class TestCDF742B(unittest.TestCase):
    def test_742B_acceptance_1(self):
        mock_input = ['2 3', '1 2']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask742BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_742B_acceptance_2(self):
        mock_input = ['6 1', '5 1 2 3 4 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask742BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

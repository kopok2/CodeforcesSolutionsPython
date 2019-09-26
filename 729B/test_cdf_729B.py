import unittest
from unittest.mock import patch

from cdf_729B import CodeforcesTask729BSolution


class TestCDF729B(unittest.TestCase):
    def test_729B_acceptance_1(self):
        mock_input = ['2 4', '0 1 0 0', '1 0 1 0']
        expected = '9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask729BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_729B_acceptance_2(self):
        mock_input = ['4 4', '0 0 0 0', '1 0 0 1', '0 1 1 0', '0 1 0 0']
        expected = '20'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask729BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

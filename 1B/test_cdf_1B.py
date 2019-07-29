import unittest
from unittest.mock import patch

from cdf_1B import CodeforcesTask1BSolution


class TestCDF1B(unittest.TestCase):
    def test_1B_acceptance_1(self):
        mock_input = ['2', 'R23C55', 'BC23']
        expected = 'BC23\nR23C55'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

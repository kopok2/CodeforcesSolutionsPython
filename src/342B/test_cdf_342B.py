import unittest
from unittest.mock import patch

from cdf_342B import CodeforcesTask342BSolution


class TestCDF342B(unittest.TestCase):
    def test_342B_acceptance_1(self):
        mock_input = ['3 5 1 3', '1 1 2', '2 2 3', '3 3 3', '4 1 1', '10 1 3']
        expected = 'XXRR'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask342BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

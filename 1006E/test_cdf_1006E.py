import unittest
from unittest.mock import patch

from cdf_1006E import CodeforcesTask1006ESolution


class TestCDF1006E(unittest.TestCase):
    def test_1006E_acceptance_1(self):
        mock_input = ['9 6', '1 1 1 3 5 3 5 7', '3 1', '1 5', '3 4', '7 3', '1 8', '1 9']
        expected = '3\n6\n8\n-1\n9\n4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006ESolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

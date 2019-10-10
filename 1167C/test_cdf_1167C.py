import unittest
from unittest.mock import patch

from cdf_1167C import CodeforcesTask1167CSolution


class TestCDF1167C(unittest.TestCase):
    def test_1167C_acceptance_1(self):
        mock_input = ['7 5 3 2 5 4 0 2 1 2 1 1 2 6 7']
        expected = '4 4 1 4 4 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1167CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

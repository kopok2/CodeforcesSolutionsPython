import unittest
from unittest.mock import patch

from cdf_340A import CodeforcesTask340ASolution


class TestCDF340A(unittest.TestCase):
    def test_340A_acceptance_1(self):
        mock_input = ['2 3 6 18']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask340ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

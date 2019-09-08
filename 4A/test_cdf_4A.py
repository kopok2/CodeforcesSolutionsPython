import unittest
from unittest.mock import patch

from cdf_4A import CodeforcesTask4ASolution


class TestCDF4A(unittest.TestCase):
    def test_4A_acceptance_1(self):
        mock_input = ['8']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask4ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

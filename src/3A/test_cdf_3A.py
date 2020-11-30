import unittest
from unittest.mock import patch

from cdf_3A import CodeforcesTask3ASolution


class TestCDF3A(unittest.TestCase):
    def test_3A_acceptance_1(self):
        mock_input = ['a8', 'h1']
        expected = '7\nRD\nRD\nRD\nRD\nRD\nRD\nRD'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask3ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

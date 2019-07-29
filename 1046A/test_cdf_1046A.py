import unittest
from unittest.mock import patch

from cdf_1046A import CodeforcesTask1046ASolution


class TestCDF1046A(unittest.TestCase):
    def test_1046A_acceptance_1(self):
        mock_input = ['3 2', '3 6 1', '7 3 10', '10 5 8']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1046ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_386B import CodeforcesTask386BSolution


class TestCDF386B(unittest.TestCase):
    def test_386B_acceptance_1(self):
        mock_input = ['6', '4 1 7 8 3 8', '1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask386BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

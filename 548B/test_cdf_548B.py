import unittest
from unittest.mock import patch

from cdf_548B import CodeforcesTask548BSolution


class TestCDF548B(unittest.TestCase):
    def test_548B_acceptance_1(self):
        mock_input = ['5 4 5', '0 1 1 0', '1 0 0 1', '0 1 1 0', '1 0 0 1', '0 0 0 0', '1 1', '1 4', '1 1', '4 2', '4 3']
        expected = '3\n4\n3\n3\n4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask548BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

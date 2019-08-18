import unittest
from unittest.mock import patch

from cdf_347B import CodeforcesTask347BSolution


class TestCDF347B(unittest.TestCase):
    def test_347B_acceptance_1(self):
        mock_input = ['5', '0 1 3 4 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask347BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_330B import CodeforcesTask330BSolution


class TestCDF330B(unittest.TestCase):
    def test_330B_acceptance_1(self):
        mock_input = ['4 1', '1 3']
        expected = '3\n1 2\n4 2\n2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask330BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

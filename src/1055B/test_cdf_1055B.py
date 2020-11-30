import unittest
from unittest.mock import patch

from cdf_1055B import CodeforcesTask1055BSolution


class TestCDF1055B(unittest.TestCase):
    def test_1055B_acceptance_1(self):
        mock_input = ['4 7 3', '1 2 3 4', '0', '1 2 3', '0', '1 1 3', '0', '1 3 1', '0']
        expected = '1\n2\n2\n1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1055BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_348B import CodeforcesTask348BSolution


class TestCDF348B(unittest.TestCase):
    def test_348B_acceptance_1(self):
        mock_input = ['6', '0 0 12 13 5 6', '1 2', '1 3', '1 4', '2 5', '2 6']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask348BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_533B import CodeforcesTask533BSolution


class TestCDF533B(unittest.TestCase):
    def test_533B_acceptance_1(self):
        mock_input = ['7', '-1 3', '1 2', '1 1', '1 4', '4 5', '4 3', '5 2']
        expected = '17'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask533BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

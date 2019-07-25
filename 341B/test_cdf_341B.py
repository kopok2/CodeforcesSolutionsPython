import unittest
from unittest.mock import patch

from cdf_341B import CodeforcesTask341BSolution


class TestCDF341B(unittest.TestCase):
    def test_341B_acceptance_1(self):
        mock_input = ['3', '3 1 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask341BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

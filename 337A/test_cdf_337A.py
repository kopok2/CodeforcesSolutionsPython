import unittest
from unittest.mock import patch

from cdf_337A import CodeforcesTask337ASolution


class TestCDF337A(unittest.TestCase):
    def test_337A_acceptance_1(self):
        mock_input = ['4 6', '10 12 10 7 5 22']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask337ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

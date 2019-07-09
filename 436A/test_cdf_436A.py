import unittest
from unittest.mock import patch

from cdf_436A import CodeforcesTask436ASolution


class TestCDF436A(unittest.TestCase):
    def test_436A_acceptance_1(self):
        mock_input = ['5 3', '0 2 4', '1 3 1', '0 8 3', '0 20 10', '1 5 5']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_274A import CodeforcesTask274ASolution


class TestCDF274A(unittest.TestCase):
    def test_274A_acceptance_1(self):
        mock_input = ['6 2', '2 3 6 5 4 10']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask274ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1140A import CodeforcesTask1140ASolution


class TestCDF1140A(unittest.TestCase):
    def test_1140A_acceptance_1(self):
        mock_input = ['9 1 3 3 6 7 6 8 8 9']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1140ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

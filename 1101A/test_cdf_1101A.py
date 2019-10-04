import unittest
from unittest.mock import patch

from cdf_1101A import CodeforcesTask1101ASolution


class TestCDF1101A(unittest.TestCase):
    def test_1101A_acceptance_1(self):
        mock_input = ['5 2 4 2 5 10 4 3 10 1 1 2 3 4 6 5']
        expected = '6 4 1 3 10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1101ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1020A import CodeforcesTask1020ASolution


class TestCDF1020A(unittest.TestCase):
    def test_1020A_acceptance_1(self):
        mock_input = ['3 6 2 3 3', '1 2 1 3', '1 4 3 4', '1 2 2 3']
        expected = '1\n4\n2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1020ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

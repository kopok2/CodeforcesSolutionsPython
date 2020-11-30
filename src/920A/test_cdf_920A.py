import unittest
from unittest.mock import patch

from cdf_920A import CodeforcesTask920ASolution


class TestCDF920A(unittest.TestCase):
    def test_920A_acceptance_1(self):
        mock_input = ['3', '5 1', '3', '3 3', '1 2 3', '4 1', '1']
        expected = '3\n1\n4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask920ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

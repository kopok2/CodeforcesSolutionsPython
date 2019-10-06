import unittest
from unittest.mock import patch

from cdf_847A import CodeforcesTask847ASolution


class TestCDF847A(unittest.TestCase):
    def test_847A_acceptance_1(self):
        mock_input = ['7', '4 7', '5 0', '0 0', '6 1', '0 2', '0 4', '1 0']
        expected = '4 7\n5 6\n0 5\n6 1\n3 2\n2 4\n1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask847ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_584A import CodeforcesTask584ASolution


class TestCDF584A(unittest.TestCase):
    def test_584A_acceptance_1(self):
        mock_input = ['3 2']
        expected = '712'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask584ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

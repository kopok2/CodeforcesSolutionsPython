import unittest
from unittest.mock import patch

from cdf_660A import CodeforcesTask660ASolution


class TestCDF660A(unittest.TestCase):
    def test_660A_acceptance_1(self):
        mock_input = ['3', '2 7 28']
        expected = '1\n2 7 9 28'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask660ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

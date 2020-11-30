import unittest
from unittest.mock import patch

from cdf_216A import CodeforcesTask216ASolution


class TestCDF216A(unittest.TestCase):
    def test_216A_acceptance_1(self):
        mock_input = ['2 3 4']
        expected = '18'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask216ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

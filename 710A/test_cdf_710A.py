import unittest
from unittest.mock import patch

from cdf_710A import CodeforcesTask710ASolution


class TestCDF710A(unittest.TestCase):
    def test_710A_acceptance_1(self):
        mock_input = ['e4']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask710ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1092A import CodeforcesTask1092ASolution


class TestCDF1092A(unittest.TestCase):
    def test_1092A_acceptance_1(self):
        mock_input = ['3 7 3 4 4 6 2']
        expected = 'cbcacab abcd baabab'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1092ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

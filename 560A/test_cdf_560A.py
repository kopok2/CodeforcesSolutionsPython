import unittest
from unittest.mock import patch

from cdf_560A import CodeforcesTask560ASolution


class TestCDF560A(unittest.TestCase):
    def test_560A_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask560ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

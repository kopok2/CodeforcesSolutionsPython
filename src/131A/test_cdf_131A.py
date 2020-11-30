import unittest
from unittest.mock import patch

from cdf_131A import CodeforcesTask131ASolution


class TestCDF131A(unittest.TestCase):
    def test_131A_acceptance_1(self):
        mock_input = ['cAPS']
        expected = 'Caps'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask131ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_131A_acceptance_2(self):
        mock_input = ['Lock']
        expected = 'Lock'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask131ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

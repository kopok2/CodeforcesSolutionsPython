import unittest
from unittest.mock import patch

from cdf_55A import CodeforcesTask55ASolution


class TestCDF55A(unittest.TestCase):
    def test_55A_acceptance_1(self):
        mock_input = ['1']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask55ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_55A_acceptance_2(self):
        mock_input = ['3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask55ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

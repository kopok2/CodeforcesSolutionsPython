import unittest
from unittest.mock import patch

from cdf_45A import CodeforcesTask45ASolution


class TestCDF45A(unittest.TestCase):
    def test_45A_acceptance_1(self):
        mock_input = ['November', '3']
        expected = 'February'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask45ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_45A_acceptance_2(self):
        mock_input = ['May', '24']
        expected = 'May'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask45ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_348A import CodeforcesTask348ASolution


class TestCDF348A(unittest.TestCase):
    def test_348A_acceptance_1(self):
        mock_input = ['3', '3 2 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask348ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_348A_acceptance_2(self):
        mock_input = ['4', '2 2 2 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask348ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

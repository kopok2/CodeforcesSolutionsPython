import unittest
from unittest.mock import patch

from cdf_391A import CodeforcesTask391ASolution


class TestCDF391A(unittest.TestCase):
    def test_391A_acceptance_1(self):
        mock_input = ['GTTAAAG']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask391ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_391A_acceptance_2(self):
        mock_input = ['AACCAACCAAAAC']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask391ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

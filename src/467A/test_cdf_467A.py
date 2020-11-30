import unittest
from unittest.mock import patch

from cdf_467A import CodeforcesTask467ASolution


class TestCDF467A(unittest.TestCase):
    def test_467A_acceptance_1(self):
        mock_input = ['3', '1 1', '2 2', '3 3']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask467ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_467A_acceptance_2(self):
        mock_input = ['3', '1 10', '0 10', '10 10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask467ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

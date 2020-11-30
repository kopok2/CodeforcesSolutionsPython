import unittest
from unittest.mock import patch

from cdf_139A import CodeforcesTask139ASolution


class TestCDF139A(unittest.TestCase):
    def test_139A_acceptance_1(self):
        mock_input = ['100', '15 20 20 15 10 30 45']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask139ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_139A_acceptance_2(self):
        mock_input = ['2', '1 0 0 0 0 0 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask139ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

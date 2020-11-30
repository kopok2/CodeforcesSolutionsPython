import unittest
from unittest.mock import patch

from cdf_259B import CodeforcesTask259BSolution


class TestCDF259B(unittest.TestCase):
    def test_259B_acceptance_1(self):
        mock_input = ['0 1 1', '1 0 1', '1 1 0']
        expected = '1 1 1\n1 1 1\n1 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask259BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_259B_acceptance_2(self):
        mock_input = ['0 3 6', '5 0 5', '4 7 0']
        expected = '6 3 6\n5 5 5\n4 7 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask259BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

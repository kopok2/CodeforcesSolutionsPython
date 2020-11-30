import unittest
from unittest.mock import patch

from cdf_546B import CodeforcesTask546BSolution


class TestCDF546B(unittest.TestCase):
    def test_546B_acceptance_1(self):
        mock_input = ['4', '1 3 1 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask546BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_546B_acceptance_2(self):
        mock_input = ['5', '1 2 3 2 5']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask546BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

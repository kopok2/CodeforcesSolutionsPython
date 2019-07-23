import unittest
from unittest.mock import patch

from cdf_8B import CodeforcesTask8BSolution


class TestCDF8B(unittest.TestCase):
    def test_8B_acceptance_1(self):
        mock_input = ['LLUUUR']
        expected = 'OK'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask8BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_8B_acceptance_2(self):
        mock_input = ['RRUULLDD']
        expected = 'BUG'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask8BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

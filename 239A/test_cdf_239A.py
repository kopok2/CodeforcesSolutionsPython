import unittest
from unittest.mock import patch

from cdf_239A import CodeforcesTask239ASolution


class TestCDF239A(unittest.TestCase):
    def test_239A_acceptance_1(self):
        mock_input = ['10 1 10']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask239ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)

    def test_239A_acceptance_2(self):
        mock_input = ['10 6 40']
        expected = '2 8 14 20 26'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask239ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()

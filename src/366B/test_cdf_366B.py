import unittest
from unittest.mock import patch

from cdf_366B import CodeforcesTask366BSolution


class TestCDF366B(unittest.TestCase):
    def test_366B_acceptance_1(self):
        mock_input = ['6 2', '3 2 1 6 5 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask366BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_366B_acceptance_2(self):
        mock_input = ['10 5', '1 3 5 7 9 9 4 1 8 5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask366BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_248B import CodeforcesTask248BSolution


class TestCDF248B(unittest.TestCase):
    def test_248B_acceptance_1(self):
        mock_input = ['1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask248BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_248B_acceptance_2(self):
        mock_input = ['5']
        expected = '10080'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask248BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

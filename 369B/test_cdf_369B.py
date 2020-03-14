import unittest
from unittest.mock import patch

from cdf_369B import CodeforcesTask369BSolution


class TestCDF369B(unittest.TestCase):
    def test_369B_acceptance_1(self):
        mock_input = ['5 3 1 3 13 9']
        expected = '2 3 2 3 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_369B_acceptance_2(self):
        mock_input = ['5 3 1 3 15 9']
        expected = '3 3 3 3 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask369BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_158B import CodeforcesTask158BSolution


class TestCDF158B(unittest.TestCase):
    def test_158B_acceptance_1(self):
        mock_input = ['5', '1 2 4 3 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask158BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_158B_acceptance_2(self):
        mock_input = ['8', '2 3 4 4 2 1 3 1']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask158BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

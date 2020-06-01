import unittest
from unittest.mock import patch

from cdf_959B import CodeforcesTask959BSolution


class TestCDF959B(unittest.TestCase):
    def test_959B_acceptance_1(self):
        mock_input = ['5 4 4', 'i loser am the second', '100 1 1 5 10', '1 1', '1 3', '2 2 5', '1 4', 'i am the second']
        expected = '107'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask959BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_959B_acceptance_2(self):
        mock_input = ['5 4 4', 'i loser am the second', '100 20 1 5 10', '1 1', '1 3', '2 2 5', '1 4', 'i am the second']
        expected = '116'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask959BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_734B import CodeforcesTask734BSolution


class TestCDF734B(unittest.TestCase):
    def test_734B_acceptance_1(self):
        mock_input = ['5 1 3 4']
        expected = '800'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask734BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_734B_acceptance_2(self):
        mock_input = ['1 1 1 1']
        expected = '256'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask734BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

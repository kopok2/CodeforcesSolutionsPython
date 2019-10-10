import unittest
from unittest.mock import patch

from cdf_378A import CodeforcesTask378ASolution


class TestCDF378A(unittest.TestCase):
    def test_378A_acceptance_1(self):
        mock_input = ['2 5']
        expected = '3 0 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask378ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_378A_acceptance_2(self):
        mock_input = ['2 4']
        expected = '2 1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask378ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

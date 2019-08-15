import unittest
from unittest.mock import patch

from cdf_887A import CodeforcesTask887ASolution


class TestCDF887A(unittest.TestCase):
    def test_887A_acceptance_1(self):
        mock_input = ['100010001']
        expected = 'yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask887ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_887A_acceptance_2(self):
        mock_input = ['100']
        expected = 'no'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask887ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

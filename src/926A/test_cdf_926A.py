import unittest
from unittest.mock import patch

from cdf_926A import CodeforcesTask926ASolution


class TestCDF926A(unittest.TestCase):
    def test_926A_acceptance_1(self):
        mock_input = ['1 10']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_926A_acceptance_2(self):
        mock_input = ['100 200']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_926A_acceptance_3(self):
        mock_input = ['1 2000000000']
        expected = '326'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask926ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

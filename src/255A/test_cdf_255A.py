import unittest
from unittest.mock import patch

from cdf_255A import CodeforcesTask255ASolution


class TestCDF255A(unittest.TestCase):
    def test_255A_acceptance_1(self):
        mock_input = ['2', '2 8']
        expected = 'biceps'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask255ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_255A_acceptance_2(self):
        mock_input = ['3', '5 1 10']
        expected = 'back'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask255ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_255A_acceptance_3(self):
        mock_input = ['7', '3 3 2 7 9 6 8']
        expected = 'chest'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask255ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

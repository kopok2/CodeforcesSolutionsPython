import unittest
from unittest.mock import patch

from cdf_394A import CodeforcesTask394ASolution


class TestCDF394A(unittest.TestCase):
    def test_394A_acceptance_1(self):
        mock_input = ['||+|=|||||']
        expected = '|||+|=||||'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_394A_acceptance_2(self):
        mock_input = ['|||||+||=||']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_394A_acceptance_3(self):
        mock_input = ['|+|=||||||']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_394A_acceptance_4(self):
        mock_input = ['||||+||=||||||']
        expected = '||||+||=||||||'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask394ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

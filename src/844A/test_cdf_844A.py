import unittest
from unittest.mock import patch

from cdf_844A import CodeforcesTask844ASolution


class TestCDF844A(unittest.TestCase):
    def test_844A_acceptance_1(self):
        mock_input = ['yandex', '6']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask844ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_844A_acceptance_2(self):
        mock_input = ['yahoo', '5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask844ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_844A_acceptance_3(self):
        mock_input = ['google', '7']
        expected = 'impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask844ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

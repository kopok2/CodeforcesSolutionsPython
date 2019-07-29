import unittest
from unittest.mock import patch

from cdf_722A import CodeforcesTask722ASolution


class TestCDF722A(unittest.TestCase):
    def test_722A_acceptance_1(self):
        mock_input = ['24', '17:30']
        expected = '17:30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_722A_acceptance_2(self):
        mock_input = ['12', '17:30']
        expected = '07:30'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_722A_acceptance_3(self):
        mock_input = ['24', '99:99']
        expected = '09:09'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask722ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

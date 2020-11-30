import unittest
from unittest.mock import patch

from cdf_506A import CodeforcesTask506ASolution


class TestCDF506A(unittest.TestCase):
    def test_506A_acceptance_1(self):
        mock_input = ['4 10', '10', '21', '27', '27']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask506ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_506A_acceptance_2(self):
        mock_input = ['8 8', '9', '19', '28', '36', '45', '55', '66', '78']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask506ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_506A_acceptance_3(self):
        mock_input = ['13 7', '8', '8', '9', '16', '17', '17', '18', '21', '23', '24', '24', '26', '30']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask506ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

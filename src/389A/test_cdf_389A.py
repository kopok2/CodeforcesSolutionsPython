import unittest
from unittest.mock import patch

from cdf_389A import CodeforcesTask389ASolution


class TestCDF389A(unittest.TestCase):
    def test_389A_acceptance_1(self):
        mock_input = ['2', '1 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask389ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_389A_acceptance_2(self):
        mock_input = ['3', '2 4 6']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask389ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_389A_acceptance_3(self):
        mock_input = ['2', '12 18']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask389ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_389A_acceptance_4(self):
        mock_input = ['5', '45 12 27 30 18']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask389ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

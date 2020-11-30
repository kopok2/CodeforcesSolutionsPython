import unittest
from unittest.mock import patch

from cdf_1141A import CodeforcesTask1141ASolution


class TestCDF1141A(unittest.TestCase):
    def test_1141A_acceptance_1(self):
        mock_input = ['120 51840']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1141A_acceptance_2(self):
        mock_input = ['42 42']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1141A_acceptance_3(self):
        mock_input = ['48 72']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1141B import CodeforcesTask1141BSolution


class TestCDF1141B(unittest.TestCase):
    def test_1141B_acceptance_1(self):
        mock_input = ['5 1 0 1 0 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1141B_acceptance_2(self):
        mock_input = ['6 0 1 0 1 1 0']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1141B_acceptance_3(self):
        mock_input = ['7 1 0 1 1 1 0 1']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1141B_acceptance_4(self):
        mock_input = ['3 0 0 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1141BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

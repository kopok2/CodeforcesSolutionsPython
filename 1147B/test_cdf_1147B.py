import unittest
from unittest.mock import patch

from cdf_1147B import CodeforcesTask1147BSolution


class TestCDF1147B(unittest.TestCase):
    def test_1147B_acceptance_1(self):
        mock_input = ['12 6 1 3 3 7 5 7 7 11 9 11 11 3']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1147BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1147B_acceptance_2(self):
        mock_input = ['9 6 4 5 5 6 7 8 8 9 1 2 2 3']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1147BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1147B_acceptance_3(self):
        mock_input = ['10 3 1 2 3 2 7 2']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1147BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1147B_acceptance_4(self):
        mock_input = ['10 2 1 6 2 7']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1147BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

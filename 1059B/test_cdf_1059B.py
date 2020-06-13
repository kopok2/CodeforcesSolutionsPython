import unittest
from unittest.mock import patch

from cdf_1059B import CodeforcesTask1059BSolution


class TestCDF1059B(unittest.TestCase):
    def test_1059B_acceptance_1(self):
        mock_input = ['3 3', '###', '#.#', '###']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1059B_acceptance_2(self):
        mock_input = ['3 3', '###', '###', '###']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1059B_acceptance_3(self):
        mock_input = ['4 3', '###', '###', '###', '###']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1059B_acceptance_4(self):
        mock_input = ['5 7', '.......', '.#####.', '.#.#.#.', '.#####.', '.......']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1059BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

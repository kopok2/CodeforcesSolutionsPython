import unittest
from unittest.mock import patch

from cdf_1102B import CodeforcesTask1102BSolution


class TestCDF1102B(unittest.TestCase):
    def test_1102B_acceptance_1(self):
        mock_input = ['4 2 1 2 2 3']
        expected = 'YES 1 1 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1102BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1102B_acceptance_2(self):
        mock_input = ['5 2 3 2 1 2 3']
        expected = 'YES 2 1 1 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1102BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1102B_acceptance_3(self):
        mock_input = ['5 2 2 1 1 2 1']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1102BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

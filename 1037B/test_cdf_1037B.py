import unittest
from unittest.mock import patch

from cdf_1037B import CodeforcesTask1037BSolution


class TestCDF1037B(unittest.TestCase):
    def test_1037B_acceptance_1(self):
        mock_input = ['3 8', '6 5 8']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1037BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1037B_acceptance_2(self):
        mock_input = ['7 20', '21 15 12 11 20 19 12']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1037BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

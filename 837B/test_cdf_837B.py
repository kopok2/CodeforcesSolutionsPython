import unittest
from unittest.mock import patch

from cdf_837B import CodeforcesTask837BSolution


class TestCDF837B(unittest.TestCase):
    def test_837B_acceptance_1(self):
        mock_input = ['6 5', 'RRRRR', 'RRRRR', 'BBBBB', 'BBBBB', 'GGGGG', 'GGGGG']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_837B_acceptance_2(self):
        mock_input = ['4 3', 'BRG', 'BRG', 'BRG', 'BRG']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_837B_acceptance_3(self):
        mock_input = ['6 7', 'RRRGGGG', 'RRRGGGG', 'RRRGGGG', 'RRRBBBB', 'RRRBBBB', 'RRRBBBB']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_837B_acceptance_4(self):
        mock_input = ['4 4', 'RRRR', 'RRRR', 'BBBB', 'GGGG']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask837BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

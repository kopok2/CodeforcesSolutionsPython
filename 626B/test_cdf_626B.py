import unittest
from unittest.mock import patch

from cdf_626B import CodeforcesTask626BSolution


class TestCDF626B(unittest.TestCase):
    def test_626B_acceptance_1(self):
        mock_input = ['2', 'RB']
        expected = 'G'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask626BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_626B_acceptance_2(self):
        mock_input = ['3', 'GRG']
        expected = 'BR'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask626BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_626B_acceptance_3(self):
        mock_input = ['5', 'BBBBB']
        expected = 'B'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask626BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

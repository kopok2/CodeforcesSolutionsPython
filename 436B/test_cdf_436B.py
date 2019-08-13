import unittest
from unittest.mock import patch

from cdf_436B import CodeforcesTask436BSolution


class TestCDF436B(unittest.TestCase):
    def test_436B_acceptance_1(self):
        mock_input = ['3 3 4', '...', 'R.L', 'R.U']
        expected = '0 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_436B_acceptance_2(self):
        mock_input = ['2 2 2', '..', 'RL']
        expected = '1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_436B_acceptance_3(self):
        mock_input = ['2 2 2', '..', 'LR']
        expected = '0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_436B_acceptance_4(self):
        mock_input = ['3 4 8', '....', 'RRLL', 'UUUU']
        expected = '1 3 3 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_436B_acceptance_5(self):
        mock_input = ['2 2 2', '..', 'UU']
        expected = '0 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask436BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

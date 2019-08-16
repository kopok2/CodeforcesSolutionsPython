import unittest
from unittest.mock import patch

from cdf_334B import CodeforcesTask334BSolution


class TestCDF334B(unittest.TestCase):
    def test_334B_acceptance_1(self):
        mock_input = ['0 0', '0 1', '0 2', '1 0', '1 2', '2 0', '2 1', '2 2']
        expected = 'respectable'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask334BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_334B_acceptance_2(self):
        mock_input = ['0 0', '1 0', '2 0', '3 0', '4 0', '5 0', '6 0', '7 0']
        expected = 'ugly'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask334BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_334B_acceptance_3(self):
        mock_input = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2']
        expected = 'ugly'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask334BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

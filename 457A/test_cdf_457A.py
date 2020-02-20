import unittest
from unittest.mock import patch

from cdf_457A import CodeforcesTask457ASolution


class TestCDF457A(unittest.TestCase):
    def test_457A_acceptance_1(self):
        mock_input = ['1000', '111']
        expected = '<'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask457ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_457A_acceptance_2(self):
        mock_input = ['00100', '11']
        expected = '='
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask457ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_457A_acceptance_3(self):
        mock_input = ['110', '101']
        expected = '>'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask457ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

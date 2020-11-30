import unittest
from unittest.mock import patch

from cdf_82B import CodeforcesTask82BSolution


class TestCDF82B(unittest.TestCase):
    def test_82B_acceptance_1(self):
        mock_input = ['4', '3 2 7 4', '3 1 7 3', '3 5 4 2', '3 1 3 5', '4 3 1 2 4', '2 5 7']
        expected = '1 7\n2 2 4\n2 1 3\n1 5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_82B_acceptance_2(self):
        mock_input = ['4', '5 6 7 8 9 100', '4 7 8 9 1', '4 7 8 9 2', '3 1 6 100', '3 2 6 100', '2 1 2']
        expected = '3 7 8 9\n2 6 100\n1 1\n1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_82B_acceptance_3(self):
        mock_input = ['3', '2 1 2', '2 1 3', '2 2 3']
        expected = '1 1\n1 2\n1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask82BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

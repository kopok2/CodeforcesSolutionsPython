import unittest
from unittest.mock import patch

from cdf_780C import CodeforcesTask780CSolution


class TestCDF780C(unittest.TestCase):
    def test_780C_acceptance_1(self):
        mock_input = ['3', '2 3', '1 3']
        expected = '3\n1 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask780CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_780C_acceptance_2(self):
        mock_input = ['5', '2 3', '5 3', '4 3', '1 3']
        expected = '5\n1 3 2 5 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask780CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_780C_acceptance_3(self):
        mock_input = ['5', '2 1', '3 2', '4 3', '5 4']
        expected = '3\n1 2 3 1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask780CSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

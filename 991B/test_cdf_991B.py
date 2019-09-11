import unittest
from unittest.mock import patch

from cdf_991B import CodeforcesTask991BSolution


class TestCDF991B(unittest.TestCase):
    def test_991B_acceptance_1(self):
        mock_input = ['3', '4 4 4']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask991BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_991B_acceptance_2(self):
        mock_input = ['4', '5 4 5 5']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask991BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_991B_acceptance_3(self):
        mock_input = ['4', '5 3 3 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask991BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

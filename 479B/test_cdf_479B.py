import unittest
from unittest.mock import patch

from cdf_479B import CodeforcesTask479BSolution


class TestCDF479B(unittest.TestCase):
    def test_479B_acceptance_1(self):
        mock_input = ['3 2', '5 8 5']
        expected = '0 2\n2 1\n2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask479BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_479B_acceptance_2(self):
        mock_input = ['3 4', '2 2 4']
        expected = '1 1\n3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask479BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_479B_acceptance_3(self):
        mock_input = ['5 3', '8 3 2 6 3']
        expected = '3 3\n1 3\n1 2\n1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask479BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

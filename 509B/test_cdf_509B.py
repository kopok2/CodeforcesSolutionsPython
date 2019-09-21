import unittest
from unittest.mock import patch

from cdf_509B import CodeforcesTask509BSolution


class TestCDF509B(unittest.TestCase):
    def test_509B_acceptance_1(self):
        mock_input = ['4 4', '1 2 3 4']
        expected = 'YES\n1\n1 4\n1 2 4\n1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask509BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_509B_acceptance_2(self):
        mock_input = ['5 2', '3 2 4 1 3']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask509BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_509B_acceptance_3(self):
        mock_input = ['5 4', '3 2 4 3 5']
        expected = 'YES\n1 2 3\n1 3\n1 2 3 4\n1 3 4\n1 1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask509BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

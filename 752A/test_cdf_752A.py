import unittest
from unittest.mock import patch

from cdf_752A import CodeforcesTask752ASolution


class TestCDF752A(unittest.TestCase):
    def test_752A_acceptance_1(self):
        mock_input = ['4 3 9']
        expected = '2 2 L'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask752ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_752A_acceptance_2(self):
        mock_input = ['4 3 24']
        expected = '4 3 R'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask752ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_752A_acceptance_3(self):
        mock_input = ['2 4 4']
        expected = '1 2 R'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask752ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

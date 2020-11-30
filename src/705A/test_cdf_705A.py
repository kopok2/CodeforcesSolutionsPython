import unittest
from unittest.mock import patch

from cdf_705A import CodeforcesTask705ASolution


class TestCDF705A(unittest.TestCase):
    def test_705A_acceptance_1(self):
        mock_input = ['1']
        expected = 'I hate it'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask705ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_705A_acceptance_2(self):
        mock_input = ['2']
        expected = 'I hate that I love it'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask705ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_705A_acceptance_3(self):
        mock_input = ['3']
        expected = 'I hate that I love that I hate it'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask705ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

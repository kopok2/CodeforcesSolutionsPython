import unittest
from unittest.mock import patch

from cdf_455A import CodeforcesTask455ASolution


class TestCDF455A(unittest.TestCase):
    def test_455A_acceptance_1(self):
        mock_input = ['2', '1 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask455ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_455A_acceptance_2(self):
        mock_input = ['3', '1 2 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask455ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_455A_acceptance_3(self):
        mock_input = ['9', '1 2 1 3 2 2 2 2 3']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask455ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

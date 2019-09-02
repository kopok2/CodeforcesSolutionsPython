import unittest
from unittest.mock import patch

from cdf_900A import CodeforcesTask900ASolution


class TestCDF900A(unittest.TestCase):
    def test_900A_acceptance_1(self):
        mock_input = ['3', '1 1', '-1 -1', '2 -1']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask900ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_900A_acceptance_2(self):
        mock_input = ['4', '1 1', '2 2', '-1 1', '-2 2']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask900ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_900A_acceptance_3(self):
        mock_input = ['3', '1 2', '2 1', '4 60']
        expected = 'Yes'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask900ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_50A import CodeforcesTask50ASolution


class TestCDF50A(unittest.TestCase):
    def test_50A_acceptance_1(self):
        mock_input = ['2 4']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask50ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_50A_acceptance_2(self):
        mock_input = ['3 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask50ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

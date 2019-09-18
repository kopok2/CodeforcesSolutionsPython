import unittest
from unittest.mock import patch

from cdf_460A import CodeforcesTask460ASolution


class TestCDF460A(unittest.TestCase):
    def test_460A_acceptance_1(self):
        mock_input = ['2 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask460ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_460A_acceptance_2(self):
        mock_input = ['9 3']
        expected = '13'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask460ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

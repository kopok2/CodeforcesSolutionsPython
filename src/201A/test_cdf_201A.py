import unittest
from unittest.mock import patch

from cdf_201A import CodeforcesTask201ASolution


class TestCDF201A(unittest.TestCase):
    def test_201A_acceptance_1(self):
        mock_input = ['4']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask201ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_201A_acceptance_2(self):
        mock_input = ['9']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask201ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

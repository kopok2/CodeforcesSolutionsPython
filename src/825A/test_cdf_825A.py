import unittest
from unittest.mock import patch

from cdf_825A import CodeforcesTask825ASolution


class TestCDF825A(unittest.TestCase):
    def test_825A_acceptance_1(self):
        mock_input = ['3', '111']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask825ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_825A_acceptance_2(self):
        mock_input = ['9', '110011101']
        expected = '2031'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask825ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

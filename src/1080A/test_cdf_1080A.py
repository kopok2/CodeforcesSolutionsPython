import unittest
from unittest.mock import patch

from cdf_1080A import CodeforcesTask1080ASolution


class TestCDF1080A(unittest.TestCase):
    def test_1080A_acceptance_1(self):
        mock_input = ['3 5']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1080ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1080A_acceptance_2(self):
        mock_input = ['15 6']
        expected = '38'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1080ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

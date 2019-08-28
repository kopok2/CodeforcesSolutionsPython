import unittest
from unittest.mock import patch

from cdf_1088A import CodeforcesTask1088ASolution


class TestCDF1088A(unittest.TestCase):
    def test_1088A_acceptance_1(self):
        mock_input = ['10']
        expected = '6 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1088ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1088A_acceptance_2(self):
        mock_input = ['1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1088ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1105A import CodeforcesTask1105ASolution


class TestCDF1105A(unittest.TestCase):
    def test_1105A_acceptance_1(self):
        mock_input = ['3 10 1 4']
        expected = '3 7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1105ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1105A_acceptance_2(self):
        mock_input = ['5 1 1 2 2 3']
        expected = '2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1105ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_687A import CodeforcesTask687ASolution


class TestCDF687A(unittest.TestCase):
    def test_687A_acceptance_1(self):
        mock_input = ['4 2', '1 2', '2 3']
        expected = '1\n2\n2\n1 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask687ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_687A_acceptance_2(self):
        mock_input = ['3 3', '1 2', '2 3', '1 3']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask687ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

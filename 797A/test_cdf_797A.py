import unittest
from unittest.mock import patch

from cdf_797A import CodeforcesTask797ASolution


class TestCDF797A(unittest.TestCase):
    def test_797A_acceptance_1(self):
        mock_input = ['100000 2']
        expected = '2 50000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask797ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_797A_acceptance_2(self):
        mock_input = ['100000 20']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask797ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_797A_acceptance_3(self):
        mock_input = ['1024 5']
        expected = '2 64 2 2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask797ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

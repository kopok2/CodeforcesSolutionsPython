import unittest
from unittest.mock import patch

from cdf_129A import CodeforcesTask129ASolution


class TestCDF129A(unittest.TestCase):
    def test_129A_acceptance_1(self):
        mock_input = ['1', '1']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_129A_acceptance_2(self):
        mock_input = ['10', '1 2 2 3 4 4 4 2 2 2']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_129A_acceptance_3(self):
        mock_input = ['11', '2 2 2 2 2 2 2 2 2 2 99']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask129ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_609A import CodeforcesTask609ASolution


class TestCDF609A(unittest.TestCase):
    def test_609A_acceptance_1(self):
        mock_input = ['3', '5', '2', '1', '3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask609ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_609A_acceptance_2(self):
        mock_input = ['3', '6', '2', '3', '2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask609ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_609A_acceptance_3(self):
        mock_input = ['2', '5', '5', '10']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask609ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

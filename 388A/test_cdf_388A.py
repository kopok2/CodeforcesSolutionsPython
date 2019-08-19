import unittest
from unittest.mock import patch

from cdf_388A import CodeforcesTask388ASolution


class TestCDF388A(unittest.TestCase):
    def test_388A_acceptance_1(self):
        mock_input = ['3', '0 0 10']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask388ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_388A_acceptance_2(self):
        mock_input = ['5', '0 1 2 3 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask388ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_388A_acceptance_3(self):
        mock_input = ['4', '0 0 0 0']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask388ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_388A_acceptance_4(self):
        mock_input = ['9', '0 1 0 2 0 1 1 2 10']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask388ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

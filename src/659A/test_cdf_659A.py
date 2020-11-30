import unittest
from unittest.mock import patch

from cdf_659A import CodeforcesTask659ASolution


class TestCDF659A(unittest.TestCase):
    def test_659A_acceptance_1(self):
        mock_input = ['6 2 -5']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask659ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_659A_acceptance_2(self):
        mock_input = ['5 1 3']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask659ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_659A_acceptance_3(self):
        mock_input = ['3 2 7']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask659ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

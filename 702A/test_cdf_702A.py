import unittest
from unittest.mock import patch

from cdf_702A import CodeforcesTask702ASolution


class TestCDF702A(unittest.TestCase):
    def test_702A_acceptance_1(self):
        mock_input = ['5', '1 7 2 11 15']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask702ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_702A_acceptance_2(self):
        mock_input = ['6', '100 100 100 100 100 100']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask702ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_702A_acceptance_3(self):
        mock_input = ['3', '1 2 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask702ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_624A import CodeforcesTask624ASolution


class TestCDF624A(unittest.TestCase):
    def test_624A_acceptance_1(self):
        mock_input = ['2 6 2 2']
        expected = '1.00000000000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask624ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_624A_acceptance_2(self):
        mock_input = ['1 9 1 2']
        expected = '2.66666666666666650000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask624ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

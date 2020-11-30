import unittest
from unittest.mock import patch

from cdf_381B import CodeforcesTask381BSolution


class TestCDF381B(unittest.TestCase):
    def test_381B_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '5\n5 4 3 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask381BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_381B_acceptance_2(self):
        mock_input = ['6', '1 1 2 2 3 3']
        expected = '5\n1 2 3 2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask381BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

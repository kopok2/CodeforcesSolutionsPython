import unittest
from unittest.mock import patch

from cdf_1060B import CodeforcesTask1060BSolution


class TestCDF1060B(unittest.TestCase):
    def test_1060B_acceptance_1(self):
        mock_input = ['35']
        expected = '17'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1060BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1060B_acceptance_2(self):
        mock_input = ['10000000000']
        expected = '91'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1060BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

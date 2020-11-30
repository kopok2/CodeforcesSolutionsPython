import unittest
from unittest.mock import patch

from cdf_624B import CodeforcesTask624BSolution


class TestCDF624B(unittest.TestCase):
    def test_624B_acceptance_1(self):
        mock_input = ['3', '2 5 5']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask624BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_624B_acceptance_2(self):
        mock_input = ['3', '1 1 2']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask624BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

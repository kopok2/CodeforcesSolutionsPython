import unittest
from unittest.mock import patch

from cdf_617B import CodeforcesTask617BSolution


class TestCDF617B(unittest.TestCase):
    def test_617B_acceptance_1(self):
        mock_input = ['3', '0 1 0']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask617BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_617B_acceptance_2(self):
        mock_input = ['5', '1 0 1 0 1']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask617BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

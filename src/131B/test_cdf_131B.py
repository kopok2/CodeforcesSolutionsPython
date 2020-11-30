import unittest
from unittest.mock import patch

from cdf_131B import CodeforcesTask131BSolution


class TestCDF131B(unittest.TestCase):
    def test_131B_acceptance_1(self):
        mock_input = ['5', '-3 3 0 0 3']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask131BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_131B_acceptance_2(self):
        mock_input = ['3', '0 0 0']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask131BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

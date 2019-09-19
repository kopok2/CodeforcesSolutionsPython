import unittest
from unittest.mock import patch

from cdf_12B import CodeforcesTask12BSolution


class TestCDF12B(unittest.TestCase):
    def test_12B_acceptance_1(self):
        mock_input = ['3310', '1033']
        expected = 'OK'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask12BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_12B_acceptance_2(self):
        mock_input = ['4', '5']
        expected = 'WRONG_ANSWER'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask12BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

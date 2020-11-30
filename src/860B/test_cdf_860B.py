import unittest
from unittest.mock import patch

from cdf_860B import CodeforcesTask860BSolution


class TestCDF860B(unittest.TestCase):
    def test_860B_acceptance_1(self):
        mock_input = ['3', '123456789', '100000000', '100123456']
        expected = '9\n000\n01'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask860BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_860B_acceptance_2(self):
        mock_input = ['4', '123456789', '193456789', '134567819', '934567891']
        expected = '2\n193\n81\n91'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask860BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

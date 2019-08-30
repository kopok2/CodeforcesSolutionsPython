import unittest
from unittest.mock import patch

from cdf_772B import CodeforcesTask772BSolution


class TestCDF772B(unittest.TestCase):
    def test_772B_acceptance_1(self):
        mock_input = ['4', '0 0', '0 1', '1 1', '1 0']
        expected = '0.3535533906'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask772BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_772B_acceptance_2(self):
        mock_input = ['6', '5 0', '10 0', '12 -4', '10 -8', '5 -8', '3 -4']
        expected = '1.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask772BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

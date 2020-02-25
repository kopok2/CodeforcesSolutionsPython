import unittest
from unittest.mock import patch

from cdf_934B import CodeforcesTask934BSolution


class TestCDF934B(unittest.TestCase):
    def test_934B_acceptance_1(self):
        mock_input = ['2']
        expected = '462'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask934BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_934B_acceptance_2(self):
        mock_input = ['6']
        expected = '8080'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask934BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

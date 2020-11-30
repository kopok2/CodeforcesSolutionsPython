import unittest
from unittest.mock import patch

from cdf_281A import CodeforcesTask281ASolution


class TestCDF281A(unittest.TestCase):
    def test_281A_acceptance_1(self):
        mock_input = ['ApPLe']
        expected = 'ApPLe'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask281ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_281A_acceptance_2(self):
        mock_input = ['konjac']
        expected = 'Konjac'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask281ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

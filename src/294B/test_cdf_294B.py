import unittest
from unittest.mock import patch

from cdf_294B import CodeforcesTask294BSolution


class TestCDF294B(unittest.TestCase):
    def test_294B_acceptance_1(self):
        mock_input = ['5', '1 12', '1 3', '2 15', '2 5', '2 1']
        expected = '5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask294BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_294B_acceptance_2(self):
        mock_input = ['3', '1 10', '2 1', '2 4']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask294BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

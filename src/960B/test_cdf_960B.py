import unittest
from unittest.mock import patch

from cdf_960B import CodeforcesTask960BSolution


class TestCDF960B(unittest.TestCase):
    def test_960B_acceptance_1(self):
        mock_input = ['2 0 0', '1 2', '2 3']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask960BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_960B_acceptance_2(self):
        mock_input = ['2 1 0', '1 2', '2 2']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask960BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_960B_acceptance_3(self):
        mock_input = ['2 5 7', '3 4', '14 4']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask960BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

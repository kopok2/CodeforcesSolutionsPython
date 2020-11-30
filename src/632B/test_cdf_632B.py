import unittest
from unittest.mock import patch

from cdf_632B import CodeforcesTask632BSolution


class TestCDF632B(unittest.TestCase):
    def test_632B_acceptance_1(self):
        mock_input = ['5', '1 2 3 4 5', 'ABABA']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask632BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_632B_acceptance_2(self):
        mock_input = ['5', '1 2 3 4 5', 'AAAAA']
        expected = '15'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask632BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_632B_acceptance_3(self):
        mock_input = ['1', '1', 'B']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask632BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

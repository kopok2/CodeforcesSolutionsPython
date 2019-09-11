import unittest
from unittest.mock import patch

from cdf_689B import CodeforcesTask689BSolution


class TestCDF689B(unittest.TestCase):
    def test_689B_acceptance_1(self):
        mock_input = ['3', '2 2 3']
        expected = '0 1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask689BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_689B_acceptance_2(self):
        mock_input = ['5', '1 2 3 4 5']
        expected = '0 1 2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask689BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_689B_acceptance_3(self):
        mock_input = ['7', '4 4 4 4 7 7 7']
        expected = '0 1 2 1 2 3 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask689BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

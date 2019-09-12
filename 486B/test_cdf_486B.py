import unittest
from unittest.mock import patch

from cdf_486B import CodeforcesTask486BSolution


class TestCDF486B(unittest.TestCase):
    def test_486B_acceptance_1(self):
        mock_input = ['2 2', '1 0', '0 0']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask486BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_486B_acceptance_2(self):
        mock_input = ['2 3', '1 1 1', '1 1 1']
        expected = 'YES\n1 1 1\n1 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask486BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_486B_acceptance_3(self):
        mock_input = ['2 3', '0 1 0', '1 1 1']
        expected = 'YES\n0 0 0\n0 1 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask486BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_975B import CodeforcesTask975BSolution


class TestCDF975B(unittest.TestCase):
    def test_975B_acceptance_1(self):
        mock_input = ['0 1 1 0 0 0 0 0 0 7 0 0 0 0']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask975BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_975B_acceptance_2(self):
        mock_input = ['5 1 1 1 1 0 0 0 0 0 0 0 0 0']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask975BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_1020B import CodeforcesTask1020BSolution


class TestCDF1020B(unittest.TestCase):
    def test_1020B_acceptance_1(self):
        mock_input = ['3', '2 3 2']
        expected = '2 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1020BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1020B_acceptance_2(self):
        mock_input = ['3', '1 2 3']
        expected = '1 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1020BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

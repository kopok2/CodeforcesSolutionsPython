import unittest
from unittest.mock import patch

from cdf_675B import CodeforcesTask675BSolution


class TestCDF675B(unittest.TestCase):
    def test_675B_acceptance_1(self):
        mock_input = ['2 1 1 1 2']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask675BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_675B_acceptance_2(self):
        mock_input = ['3 3 1 2 3']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask675BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_165B import CodeforcesTask165BSolution


class TestCDF165B(unittest.TestCase):
    def test_165B_acceptance_1(self):
        mock_input = ['7 2']
        expected = '4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask165BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_165B_acceptance_2(self):
        mock_input = ['59 9']
        expected = '54'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask165BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

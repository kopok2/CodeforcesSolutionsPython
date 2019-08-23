import unittest
from unittest.mock import patch

from cdf_402B import CodeforcesTask402BSolution


class TestCDF402B(unittest.TestCase):
    def test_402B_acceptance_1(self):
        mock_input = ['4 1', '1 2 1 5']
        expected = '2\n+ 3 2\n- 4 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask402BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_402B_acceptance_2(self):
        mock_input = ['4 1', '1 2 3 4']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask402BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

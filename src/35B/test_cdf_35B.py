import unittest
from unittest.mock import patch

from cdf_35B import CodeforcesTask35BSolution


class TestCDF35B(unittest.TestCase):
    def test_35B_acceptance_1(self):
        mock_input = ['2 2 9', '+1 1 1 cola', '+1 1 1 fanta', '+1 1 1 sevenup', '+1 1 1 whitekey', '-1 cola', '-1 fanta', '-1 sevenup', '-1 whitekey', '-1 cola']
        expected = '1 1\n1 2\n2 1\n2 2\n-1 -1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask35BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_35B_acceptance_2(self):
        mock_input = ['2 2 8', '+1 1 1 cola', '-1 cola', '+1 1 1 fanta', '-1 fanta', '+1 1 1 sevenup', '-1 sevenup', '+1 1 1 whitekey', '-1 whitekey']
        expected = '1 1\n1 1\n1 1\n1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask35BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

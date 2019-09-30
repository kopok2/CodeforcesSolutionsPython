import unittest
from unittest.mock import patch

from cdf_352B import CodeforcesTask352BSolution


class TestCDF352B(unittest.TestCase):
    def test_352B_acceptance_1(self):
        mock_input = ['1', '2']
        expected = '1\n2 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask352BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_352B_acceptance_2(self):
        mock_input = ['8', '1 2 1 3 1 2 1 5']
        expected = '4\n1 2\n2 4\n3 0\n5 0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask352BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

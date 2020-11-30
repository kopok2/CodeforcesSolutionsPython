import unittest
from unittest.mock import patch

from cdf_68B import CodeforcesTask68BSolution


class TestCDF68B(unittest.TestCase):
    def test_68B_acceptance_1(self):
        mock_input = ['3 50', '4 2 1']
        expected = '2.000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask68BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_68B_acceptance_2(self):
        mock_input = ['2 90', '1 11']
        expected = '1.909090909'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask68BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

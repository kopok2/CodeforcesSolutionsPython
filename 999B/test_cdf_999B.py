import unittest
from unittest.mock import patch

from cdf_999B import CodeforcesTask999BSolution


class TestCDF999B(unittest.TestCase):
    def test_999B_acceptance_1(self):
        mock_input = ['10', 'rocesfedoc']
        expected = 'codeforces'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_999B_acceptance_2(self):
        mock_input = ['16', 'plmaetwoxesisiht']
        expected = 'thisisexampletwo'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_999B_acceptance_3(self):
        mock_input = ['1', 'z']
        expected = 'z'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask999BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

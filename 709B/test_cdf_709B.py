import unittest
from unittest.mock import patch

from cdf_709B import CodeforcesTask709BSolution


class TestCDF709B(unittest.TestCase):
    def test_709B_acceptance_1(self):
        mock_input = ['3 10', '1 7 12']
        expected = '7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask709BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_709B_acceptance_2(self):
        mock_input = ['2 0', '11 -10']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask709BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_709B_acceptance_3(self):
        mock_input = ['5 0', '0 0 1000 0 0']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask709BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

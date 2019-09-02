import unittest
from unittest.mock import patch

from cdf_439B import CodeforcesTask439BSolution


class TestCDF439B(unittest.TestCase):
    def test_439B_acceptance_1(self):
        mock_input = ['2 3', '4 1']
        expected = '11'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask439BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_439B_acceptance_2(self):
        mock_input = ['4 2', '5 1 2 1']
        expected = '10'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask439BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_439B_acceptance_3(self):
        mock_input = ['3 3', '1 1 1']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask439BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

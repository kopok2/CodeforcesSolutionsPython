import unittest
from unittest.mock import patch

from cdf_782B import CodeforcesTask782BSolution


class TestCDF782B(unittest.TestCase):
    def test_782B_acceptance_1(self):
        mock_input = ['3', '7 1 3', '1 2 1']
        expected = '2.000000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask782BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_782B_acceptance_2(self):
        mock_input = ['4', '5 10 3 2', '2 3 2 4']
        expected = '1.400000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask782BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

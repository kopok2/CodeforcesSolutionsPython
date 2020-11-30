import unittest
from unittest.mock import patch

from cdf_766B import CodeforcesTask766BSolution


class TestCDF766B(unittest.TestCase):
    def test_766B_acceptance_1(self):
        mock_input = ['5', '1 5 3 2 4']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask766BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_766B_acceptance_2(self):
        mock_input = ['3', '4 1 2']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask766BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

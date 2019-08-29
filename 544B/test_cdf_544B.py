import unittest
from unittest.mock import patch

from cdf_544B import CodeforcesTask544BSolution


class TestCDF544B(unittest.TestCase):
    def test_544B_acceptance_1(self):
        mock_input = ['5 2']
        expected = 'YES\nSSSSS\nLLLLL\nSSSSS\nLLLLL\nSSSSS'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask544BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_544B_acceptance_2(self):
        mock_input = ['5 25']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask544BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

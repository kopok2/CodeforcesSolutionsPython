import unittest
from unittest.mock import patch

from cdf_49B import CodeforcesTask49BSolution


class TestCDF49B(unittest.TestCase):
    def test_49B_acceptance_1(self):
        mock_input = ['78 87']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask49BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_49B_acceptance_2(self):
        mock_input = ['1 1']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask49BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

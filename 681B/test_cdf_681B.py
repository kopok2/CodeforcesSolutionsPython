import unittest
from unittest.mock import patch

from cdf_681B import CodeforcesTask681BSolution


class TestCDF681B(unittest.TestCase):
    def test_681B_acceptance_1(self):
        mock_input = ['1359257']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask681BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_681B_acceptance_2(self):
        mock_input = ['17851817']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask681BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

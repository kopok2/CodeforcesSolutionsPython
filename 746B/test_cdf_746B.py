import unittest
from unittest.mock import patch

from cdf_746B import CodeforcesTask746BSolution


class TestCDF746B(unittest.TestCase):
    def test_746B_acceptance_1(self):
        mock_input = ['5', 'logva']
        expected = 'volga'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask746BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_746B_acceptance_2(self):
        mock_input = ['2', 'no']
        expected = 'no'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask746BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_746B_acceptance_3(self):
        mock_input = ['4', 'abba']
        expected = 'baba'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask746BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_940B import CodeforcesTask940BSolution


class TestCDF940B(unittest.TestCase):
    def test_940B_acceptance_1(self):
        mock_input = ['9', '2', '3', '1']
        expected = '6'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask940BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_940B_acceptance_2(self):
        mock_input = ['5', '5', '2', '20']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask940BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_940B_acceptance_3(self):
        mock_input = ['19', '3', '4', '2']
        expected = '12'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask940BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

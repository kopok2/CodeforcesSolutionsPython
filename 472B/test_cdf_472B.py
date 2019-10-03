import unittest
from unittest.mock import patch

from cdf_472B import CodeforcesTask472BSolution


class TestCDF472B(unittest.TestCase):
    def test_472B_acceptance_1(self):
        mock_input = ['3 2', '2 3 4']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask472BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_472B_acceptance_2(self):
        mock_input = ['4 2', '50 100 50 100']
        expected = '296'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask472BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_472B_acceptance_3(self):
        mock_input = ['10 3', '2 2 2 2 2 2 2 2 2 2']
        expected = '8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask472BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

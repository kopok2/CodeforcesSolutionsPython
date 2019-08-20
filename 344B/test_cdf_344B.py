import unittest
from unittest.mock import patch

from cdf_344B import CodeforcesTask344BSolution


class TestCDF344B(unittest.TestCase):
    def test_344B_acceptance_1(self):
        mock_input = ['1 1 2']
        expected = '0 1 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask344BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_344B_acceptance_2(self):
        mock_input = ['3 4 5']
        expected = '1 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask344BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_344B_acceptance_3(self):
        mock_input = ['4 1 1']
        expected = 'Impossible'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask344BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

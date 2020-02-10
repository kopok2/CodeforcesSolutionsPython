import unittest
from unittest.mock import patch

from cdf_106A import CodeforcesTask106ASolution


class TestCDF106A(unittest.TestCase):
    def test_106A_acceptance_1(self):
        mock_input = ['H', 'QH 9S']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_106A_acceptance_2(self):
        mock_input = ['S', '8D 6D']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_106A_acceptance_3(self):
        mock_input = ['C', '7H AS']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask106ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

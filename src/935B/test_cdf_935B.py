import unittest
from unittest.mock import patch

from cdf_935B import CodeforcesTask935BSolution


class TestCDF935B(unittest.TestCase):
    def test_935B_acceptance_1(self):
        mock_input = ['1', 'U']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask935BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_935B_acceptance_2(self):
        mock_input = ['6', 'RURUUR']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask935BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_935B_acceptance_3(self):
        mock_input = ['7', 'URRRUUU']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask935BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

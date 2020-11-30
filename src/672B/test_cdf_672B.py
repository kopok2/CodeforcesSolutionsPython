import unittest
from unittest.mock import patch

from cdf_672B import CodeforcesTask672BSolution


class TestCDF672B(unittest.TestCase):
    def test_672B_acceptance_1(self):
        mock_input = ['2', 'aa']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask672BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_672B_acceptance_2(self):
        mock_input = ['4', 'koko']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask672BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_672B_acceptance_3(self):
        mock_input = ['5', 'murat']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask672BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

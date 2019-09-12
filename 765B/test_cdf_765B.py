import unittest
from unittest.mock import patch

from cdf_765B import CodeforcesTask765BSolution


class TestCDF765B(unittest.TestCase):
    def test_765B_acceptance_1(self):
        mock_input = ['abacaba']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask765BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_765B_acceptance_2(self):
        mock_input = ['jinotega']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask765BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

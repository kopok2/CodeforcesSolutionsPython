import unittest
from unittest.mock import patch

from cdf_47B import CodeforcesTask47BSolution


class TestCDF47B(unittest.TestCase):
    def test_47B_acceptance_1(self):
        mock_input = ['A>B', 'C<B', 'A>C']
        expected = 'CBA'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask47BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_47B_acceptance_2(self):
        mock_input = ['A<B', 'B>C', 'C>A']
        expected = 'ACB'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask47BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

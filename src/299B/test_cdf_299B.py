import unittest
from unittest.mock import patch

from cdf_299B import CodeforcesTask299BSolution


class TestCDF299B(unittest.TestCase):
    def test_299B_acceptance_1(self):
        mock_input = ['2 1', '..']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask299BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_299B_acceptance_2(self):
        mock_input = ['5 2', '.#.#.']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask299BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_299B_acceptance_3(self):
        mock_input = ['7 3', '.#.###.']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask299BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

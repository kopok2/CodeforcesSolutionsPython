import unittest
from unittest.mock import patch

from cdf_519A import CodeforcesTask519ASolution


class TestCDF519A(unittest.TestCase):
    def test_519A_acceptance_1(self):
        mock_input = ['...QK...', '........', '........', '........', '........', '........', '........', '...rk...']
        expected = 'White'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask519ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_519A_acceptance_2(self):
        mock_input = ['rnbqkbnr', 'pppppppp', '........', '........', '........', '........', 'PPPPPPPP', 'RNBQKBNR']
        expected = 'Draw'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask519ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_519A_acceptance_3(self):
        mock_input = ['rppppppr', '...k....', '........', '........', '........', '........', 'K...Q...', '........']
        expected = 'Black'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask519ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

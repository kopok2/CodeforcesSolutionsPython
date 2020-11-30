import unittest
from unittest.mock import patch

from cdf_592A import CodeforcesTask592ASolution


class TestCDF592A(unittest.TestCase):
    def test_592A_acceptance_1(self):
        mock_input = ['........', '........', '.B....B.', '....W...', '........', '..W.....', '........', '........']
        expected = 'A'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask592ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_592A_acceptance_2(self):
        mock_input = ['..B.....', '..W.....', '......B.', '........', '.....W..', '......B.', '........', '........']
        expected = 'B'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask592ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_404A import CodeforcesTask404ASolution


class TestCDF404A(unittest.TestCase):
    def test_404A_acceptance_1(self):
        mock_input = ['5', 'xooox', 'oxoxo', 'soxoo', 'oxoxo', 'xooox']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask404ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_404A_acceptance_2(self):
        mock_input = ['3', 'wsw', 'sws', 'wsw']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask404ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_404A_acceptance_3(self):
        mock_input = ['3', 'xpx', 'pxp', 'xpe']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask404ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_776A import CodeforcesTask776ASolution


class TestCDF776A(unittest.TestCase):
    def test_776A_acceptance_1(self):
        mock_input = ['ross rachel', '4', 'ross joey', 'rachel phoebe', 'phoebe monica', 'monica chandler']
        expected = 'ross rachel\njoey rachel\njoey phoebe\njoey monica\njoey chandler'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask776ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_776A_acceptance_2(self):
        mock_input = ['icm codeforces', '1', 'codeforces technex']
        expected = 'icm codeforces\nicm technex'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask776ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

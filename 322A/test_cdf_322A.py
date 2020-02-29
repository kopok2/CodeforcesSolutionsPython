import unittest
from unittest.mock import patch

from cdf_322A import CodeforcesTask322ASolution


class TestCDF322A(unittest.TestCase):
    def test_322A_acceptance_1(self):
        mock_input = ['2 1']
        expected = '2\n1 1\n2 1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask322ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_322A_acceptance_2(self):
        mock_input = ['2 2']
        expected = '3\n1 1\n1 2\n2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask322ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

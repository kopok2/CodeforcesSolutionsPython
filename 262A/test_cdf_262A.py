import unittest
from unittest.mock import patch

from cdf_262A import CodeforcesTask262ASolution


class TestCDF262A(unittest.TestCase):
    def test_262A_acceptance_1(self):
        mock_input = ['3 4', '1 2 4']
        expected = '3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask262ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_262A_acceptance_2(self):
        mock_input = ['3 2', '447 44 77']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask262ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

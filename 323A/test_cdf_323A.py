import unittest
from unittest.mock import patch

from cdf_323A import CodeforcesTask323ASolution


class TestCDF323A(unittest.TestCase):
    def test_323A_acceptance_1(self):
        mock_input = ['1']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask323ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_323A_acceptance_2(self):
        mock_input = ['2']
        expected = 'bb\nww\n\nbb\nww'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask323ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

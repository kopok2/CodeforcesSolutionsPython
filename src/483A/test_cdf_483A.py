import unittest
from unittest.mock import patch

from cdf_483A import CodeforcesTask483ASolution


class TestCDF483A(unittest.TestCase):
    def test_483A_acceptance_1(self):
        mock_input = ['2 4']
        expected = '2 3 4'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask483ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_483A_acceptance_2(self):
        mock_input = ['10 11']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask483ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_483A_acceptance_3(self):
        mock_input = ['900000000000000009 900000000000000029']
        expected = '900000000000000009 900000000000000010 900000000000000021'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask483ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

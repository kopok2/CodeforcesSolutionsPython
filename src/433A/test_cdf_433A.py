import unittest
from unittest.mock import patch

from cdf_433A import CodeforcesTask433ASolution


class TestCDF433A(unittest.TestCase):
    def test_433A_acceptance_1(self):
        mock_input = ['3', '100 200 100']
        expected = 'YES'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask433ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_433A_acceptance_2(self):
        mock_input = ['4', '100 100 100 200']
        expected = 'NO'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask433ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

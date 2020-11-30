import unittest
from unittest.mock import patch

from cdf_174A import CodeforcesTask174ASolution


class TestCDF174A(unittest.TestCase):
    def test_174A_acceptance_1(self):
        mock_input = ['5 50', '1 2 3 4 5']
        expected = '12.000000\n11.000000\n10.000000\n9.000000\n8.000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask174ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_174A_acceptance_2(self):
        mock_input = ['2 2', '1 100']
        expected = '-1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask174ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

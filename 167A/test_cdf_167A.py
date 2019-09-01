import unittest
from unittest.mock import patch

from cdf_167A import CodeforcesTask167ASolution


class TestCDF167A(unittest.TestCase):
    def test_167A_acceptance_1(self):
        mock_input = ['3 10 10000', '0 10', '5 11', '1000 1']
        expected = '1000.5000000000\n1000.5000000000\n11000.0500000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask167ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_167A_acceptance_2(self):
        mock_input = ['1 2 26', '28 29']
        expected = '33.0990195136'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask167ASolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

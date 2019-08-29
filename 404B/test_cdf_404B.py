import unittest
from unittest.mock import patch

from cdf_404B import CodeforcesTask404BSolution


class TestCDF404B(unittest.TestCase):
    def test_404B_acceptance_1(self):
        mock_input = ['2 5', '2']
        expected = '1.0000000000 2.0000000000\n2.0000000000 0.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask404BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_404B_acceptance_2(self):
        mock_input = ['4.147 2.8819', '6']
        expected = '2.8819000000 0.0000000000\n4.1470000000 1.6168000000\n3.7953000000 4.1470000000\n0.9134000000 4.1470000000\n0.0000000000 2.1785000000\n0.7034000000 0.0000000000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask404BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

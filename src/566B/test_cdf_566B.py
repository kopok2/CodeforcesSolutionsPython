import unittest
from unittest.mock import patch

from cdf_566B import CodeforcesTask566BSolution


class TestCDF566B(unittest.TestCase):
    def test_566B_acceptance_1(self):
        mock_input = ['2', '1 2 2', '1 2 2', '1 2 2', '1 2 2', '2 1 1', '2 1 1', '2 1 1', '2 1 1']
        expected = 'YES\n1 2 5 6 3 7 4 8'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask566BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_566B_acceptance_2(self):
        mock_input = ['3', '1 2 3', '1 1 1', '1 1 1', '1 1 1', '2 1 3', '2 2 2', '2 2 2', '2 2 2', '3 1 2', '3 3 3', '3 3 3', '3 3 3']
        expected = 'YES\n2 3 4 6 7 8 10 11 12 1 5 9'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask566BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

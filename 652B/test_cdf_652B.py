import unittest
from unittest.mock import patch

from cdf_652B import CodeforcesTask652BSolution


class TestCDF652B(unittest.TestCase):
    def test_652B_acceptance_1(self):
        mock_input = ['4', '1 2 2 1']
        expected = '1 2 1 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask652BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_652B_acceptance_2(self):
        mock_input = ['5', '1 3 2 2 5']
        expected = '1 5 2 3 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask652BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

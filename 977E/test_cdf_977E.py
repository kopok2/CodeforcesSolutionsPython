import unittest
from unittest.mock import patch

from cdf_977E import CodeforcesTask977ESolution


class TestCDF977E(unittest.TestCase):
    def test_977E_acceptance_1(self):
        mock_input = ['5 4', '1 2', '3 4', '5 4', '3 5']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask977ESolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_977E_acceptance_2(self):
        mock_input = ['17 15', '1 8', '1 12', '5 11', '11 9', '9 15', '15 5', '4 13', '3 13', '4 3', '10 16', '7 10', '16 7', '14 3', '14 4', '17 6']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask977ESolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

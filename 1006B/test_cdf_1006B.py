import unittest
from unittest.mock import patch

from cdf_1006B import CodeforcesTask1006BSolution


class TestCDF1006B(unittest.TestCase):
    def test_1006B_acceptance_1(self):
        mock_input = ['8 3', '5 4 2 6 5 1 9 2']
        expected = '20\n3 2 3'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1006B_acceptance_2(self):
        mock_input = ['5 1', '1 1 1 1 1']
        expected = '1\n5'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1006B_acceptance_3(self):
        mock_input = ['4 2', '1 2000 2000 2']
        expected = '4000\n2 2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1006BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

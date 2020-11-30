import unittest
from unittest.mock import patch

from cdf_1028B import CodeforcesTask1028BSolution


class TestCDF1028B(unittest.TestCase):
    def test_1028B_acceptance_1(self):
        mock_input = ['6 5']
        expected = '6\n7'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1028BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_1028B_acceptance_2(self):
        mock_input = ['8 16']
        expected = '35\n53'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask1028BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

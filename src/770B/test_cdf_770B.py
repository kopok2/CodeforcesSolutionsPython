import unittest
from unittest.mock import patch

from cdf_770B import CodeforcesTask770BSolution


class TestCDF770B(unittest.TestCase):
    def test_770B_acceptance_1(self):
        mock_input = ['100']
        expected = '99'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask770BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_770B_acceptance_2(self):
        mock_input = ['48']
        expected = '48'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask770BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_770B_acceptance_3(self):
        mock_input = ['521']
        expected = '499'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask770BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

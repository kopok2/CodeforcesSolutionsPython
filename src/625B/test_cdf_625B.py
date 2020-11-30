import unittest
from unittest.mock import patch

from cdf_625B import CodeforcesTask625BSolution


class TestCDF625B(unittest.TestCase):
    def test_625B_acceptance_1(self):
        mock_input = ['intellect', 'tell']
        expected = '1'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask625BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_625B_acceptance_2(self):
        mock_input = ['google', 'apple']
        expected = '0'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask625BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_625B_acceptance_3(self):
        mock_input = ['sirisiri', 'sir']
        expected = '2'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask625BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

from cdf_989B import CodeforcesTask989BSolution


class TestCDF989B(unittest.TestCase):
    def test_989B_acceptance_1(self):
        mock_input = ['10 7', '1.0.1.0.1.']
        expected = '1000100010'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask989BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_989B_acceptance_2(self):
        mock_input = ['10 6', '1.0.1.1000']
        expected = '1001101000'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask989BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)

    def test_989B_acceptance_3(self):
        mock_input = ['10 9', '1........1']
        expected = 'No'
        with patch('builtins.input', side_effect=mock_input):
            Solution = CodeforcesTask989BSolution()
            Solution.read_input()
            Solution.process_task()
            actual = Solution.get_result()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
